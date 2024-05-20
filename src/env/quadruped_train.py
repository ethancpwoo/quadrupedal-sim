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
from utils.graph import Grapher
from utils.ornstienUhlenbeck import OU
from utils.update_target import Updater
from utils.replayBuffer import ReplayBuffer
from tqdm import tqdm


device = "cuda:0" if torch.cuda.is_available() else 'cpu'

# ==============================================================

BATCH_SIZE = 149
BUFFER_SIZE = 100000
EXPLORE = 50000
GAMMA = 0.99
MAX_EPISODES = 3000
TAU = 0.001

buff = ReplayBuffer(BUFFER_SIZE)
# env = QuadrupedEnv(render_mode='GUI')
env = QuadrupedEnv(render_mode='direct')
grapher = Grapher()
updater = Updater()
epsilon = 1.0
orn_uhlen = OU()

actor_losses = []
critic_losses = []
epsilons = []
reward_acc = []
step_count = []
roll = [] # First index
pitch = [] # Second index
yaw = [] # Third index

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

#TODO: graph, verify LR and verify and adjust reward values with extreme prejudice

for episode in tqdm(range(MAX_EPISODES)):
    obs = env.reset()
    cur_state = obs
    obs = torch.Tensor(obs).cuda()

    episode_actor_losses = []
    episode_critic_losses = []
    episode_epsilons = []
    episode_rewards = []

    while True: 
        epsilon -= 1.0/ EXPLORE
        episode_epsilons.append(epsilon)
        loss = 0

        action = actor.forward(obs)
        action = action.cpu().detach().numpy()
        noise = np.array([max(epsilon, 0) * orn_uhlen.OU(action[x], 0, 1, 0.3) for x in range(12)]).flatten()
        action = np.add(action, noise)

        obs, reward, done = env.step(action=action)
        episode_rewards.append(reward)

        new_state = obs
        obs = torch.Tensor(obs).cuda()

        buff.add(cur_state, action, reward, new_state, done)

        batch = buff.get_batch(BATCH_SIZE)
        
        states = np.asarray([x[0] for x in batch])
        actions = np.asarray([x[1] for x in batch])
        rewards = np.asarray([x[2] for x in batch])
        new_states = np.asarray([x[3] for x in batch])
        dones = np.asarray([x[4] for x in batch])

        # pass new_states, and actor prediction from new_states, should be the target critic network
        new_states = torch.from_numpy(new_states)
        new_states = new_states.to(torch.float32).cuda()
        next_q_values = critic_target.forward(new_states, actor_target(new_states))
        next_q_values = next_q_values.cpu().detach().numpy().flatten()

        target_q_batch = rewards + (GAMMA * dones * next_q_values)
        target_q_batch = np.array(target_q_batch)
        target_q_batch = torch.from_numpy(target_q_batch).to(torch.float32).cuda()

        # Recheck new q_batch and the loss...\
        states = torch.from_numpy(states).to(torch.float32).cuda()
        actions = torch.from_numpy(actions).to(torch.float32).cuda()

        critic.zero_grad()
        q_batch = critic(states, actions).flatten()
        value_loss = critic.loss(q_batch, target_q_batch)
        value_loss.backward()
        critic.optimizer.step()

        actor.zero_grad()
        policy_loss = -critic(states, actor(states))
        policy_loss = policy_loss.mean()
        policy_loss.backward()
        actor.optimizer.step()

        episode_critic_losses.append(value_loss.cpu().detach().numpy())
        episode_actor_losses.append(policy_loss.cpu().detach().numpy())

        updater.update_target(actor_target, actor, TAU)
        updater.update_target(critic_target, critic, TAU)

        if done: 
            break
    
    actor_losses.append(np.mean(episode_actor_losses))
    critic_losses.append(np.mean(episode_critic_losses))
    epsilons.append(np.mean(episode_epsilons))
    reward_acc.append(np.mean(np.array(episode_rewards).flatten()))

p.disconnect()

grapher.graph_params(reward_acc, env.final_positions, actor_losses, critic_losses, env.reward_vel, env.reward_time, env.reward_height, env.reward_rotations)

torch.save(actor.state_dict(), './saved_models/actor.pt')
torch.save(critic.state_dict(), './saved_models/critic.pt')
torch.save(actor_target.state_dict(), './saved_models/actor_target.pt')
torch.save(critic_target.state_dict(), './saved_models/critic_target.pt')

eval.eval()

print("done")
