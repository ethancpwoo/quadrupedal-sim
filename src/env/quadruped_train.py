import eval
import gymnasium as gym
import numpy as np
import pybullet as p
import torch
import torch.nn as nn
import torch.nn.functional as F

from models.actor import Actor
from models.critic import Critic
from quadruped_env import QuadrupedEnv
from utils.replayBuffer import ReplayBuffer
from utils.ornstienUhlenbeck import OU
from utils.update_target import Updater
from tqdm import tqdm


device = "cuda:0" if torch.cuda.is_available() else 'cpu'

# ==============================================================

BATCH_SIZE = 41
BUFFER_SIZE = 100000
EXPLORE = 100000
GAMMA = 0.99
MAX_EPISODES = 1000
TAU = 0.001

buff = ReplayBuffer(BUFFER_SIZE)
# env = QuadrupedEnv(render_mode='GUI')
env = QuadrupedEnv(render_mode='direct')
updater = Updater()
epsilon = 1.0
orn_uhlen = OU()
training = True

actor = Actor()
critic = Critic()
actor_target = Actor()
critic_target = Critic()
actor = actor.to(device=device)
critic = critic.to(device=device)
actor_target = actor_target.to(device=device)
critic_target = critic_target.to(device=device)

updater.equate_model(actor_target, actor)
updater.equate_model(critic_target, critic)

#TODO: need to map values correctly to DOF ranges, verify LR and verify and adjust reward values with extreme prejudice

for episode in tqdm(range(MAX_EPISODES)):
    obs = env.reset()
    cur_state = obs
    obs = torch.Tensor(obs).cuda()

    while True: 
        epsilon -= 1.0/ EXPLORE
        loss = 0

        action = actor(obs)
        action = action.cpu().detach().numpy()
        noise = np.array([max(epsilon, 0) * orn_uhlen.OU(action[x], 0.5, 1, 0.1) for x in range(12)]).flatten()
        # print(action)
        # print(noise)
        action = np.add(action, noise)

        # should add OU noise for each action for exploration

        # print('action: \n')
        # print(action)
        obs, reward, done = env.step(action=action)
        
        # should add replay buffer for random sampling of critic
        new_state = obs
        obs = torch.Tensor(obs).cuda()

        buff.add(cur_state, action, reward, new_state, done)

        batch = buff.get_batch(BATCH_SIZE)
        
        states = np.asarray([x[0] for x in batch])
        actions = np.asarray([x[1] for x in batch])
        rewards = np.asarray([x[2] for x in batch])
        new_states = np.asarray([x[3] for x in batch])
        dones = np.asarray([x[4] for x in batch])
        new_q_batch = []

        # pass new_states, and actor prediction from new_states, should be the target critic network
        new_states = torch.from_numpy(new_states)
        new_states = new_states.to(torch.float32).cuda()
        target_q_values = critic_target(new_states, actor_target(new_states))
        target_q_values = target_q_values.cpu().detach().numpy().flatten()

        # print(rewards)
        # print(target_q_values)

        for i in range(len(batch)):
            if dones[i]:
                new_q_batch.append(rewards[i])
            else:
                new_q_batch.append(rewards[i] + GAMMA*target_q_values[i])
        
        # print(new_q_batch)

        new_q_batch = np.array(new_q_batch)
        new_q_batch = torch.from_numpy(new_q_batch).to(torch.float32).cuda()

        if training:
            critic.train(states, actions, new_q_batch)

            states = torch.Tensor(states).cuda()
            critic_out = -critic(states, actor(states))

            actor.train(critic_out)
            updater.update_target(actor_target, actor, TAU)
            updater.update_target(critic_target, critic, TAU)

            # weights into targets
        # print(f'\n num steps: {buff.num_added}')

        if done: 
            break        

p.disconnect()

torch.save(actor.state_dict(), './saved_models/actor.pt')
torch.save(critic.state_dict(), './saved_models/critic.pt')
torch.save(actor_target.state_dict(), './saved_models/actor_target.pt')
torch.save(critic_target.state_dict(), './saved_models/critic_target.pt')

eval.eval()

print("done")
