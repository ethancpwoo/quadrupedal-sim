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


device = 'cuda' if torch.cuda.is_available() else 'cpu'

# ==============================================================

MAX_EPISODES = 1
BATCH_SIZE = 32
GAMMA = 0.99

env = QuadrupedEnv()
actor = Actor()
critic = Critic()
buff = ReplayBuffer(MAX_EPISODES)

training = True

#TODO: need to convert to np arrays more and refrain from tensors unless necessary

for episode in range(MAX_EPISODES):
    obs = env.reset()
    obs = torch.Tensor(obs)
    cur_state = obs

    while True: 
        loss = 0

        action = actor(obs)
        action = action.detach().numpy()
        # should add OU noise for each action for exploration
        obs, reward, done = env.step(action=action)
        
        # should add replay buffer for random sampling of critic
        new_state = obs
        obs = torch.Tensor(obs)
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
        new_states = new_states.to(torch.float32)
        target_q_values = critic(new_states, actor(new_states))
        target_q_values = target_q_values.detach().numpy()

        for i in range(len(batch)):
            if dones[i]:
                new_q_batch.append(rewards[i])
            else:
                new_q_batch.append(rewards[i] + GAMMA*target_q_values[i])
            new_q_batch = torch.Tensor(new_q_batch)

        if training:
            critic.train(states, actions, new_q_batch)

            states = torch.Tensor(states)
            critic_out = -critic(states, actor(states))

            actor.train(critic_out)

            # weights into targets

        if done: 
            break        

print("done")
