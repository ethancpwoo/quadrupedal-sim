import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from actor import Actor
from critic import Critic
from quadruped_env import QuadrupedEnv
from utils.replayBuffer import ReplayBuffer
from tqdm import tqdm


device = "cuda:0" if torch.cuda.is_available() else 'cpu'

# ==============================================================

MAX_EPISODES = 1
BATCH_SIZE = 41
GAMMA = 0.99
BUFFER_SIZE = 100000

env = QuadrupedEnv()
actor = Actor()
critic = Critic()
actor = actor.to(device=device)
critic = critic.to(device=device)
buff = ReplayBuffer(BUFFER_SIZE)

training = True

#TODO: need to convert to np arrays more and refrain from tensors unless necessary

for episode in range(MAX_EPISODES):
    obs = env.reset()
    cur_state = obs
    obs = torch.Tensor(obs).cuda()

    while True: 
        loss = 0

        action = actor(obs)
        action = action.cpu().detach().numpy()
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
        target_q_values = critic(new_states, actor(new_states))
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

            # weights into targets
        print(f'\n num steps: {buff.num_added}')
        if done: 
            break        

print("done")
