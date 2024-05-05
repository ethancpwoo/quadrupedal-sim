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
gamma = 0.9

def update_agent(agent, rewards, log_probs):
    drs = []

    for i in range(len(rewards)):
        total = 0
        pw = 0
        for reward in rewards[i:]:
            total += gamma**pw * reward
            pw += 1
        drs.append(total)
    
    drs -= np.mean(drs)
    drs /= np.std(drs)
    drs = torch.tensor(drs)

    pg = []
    for log_prob, gt in zip(log_probs, drs):
        pg.append(-log_prob * gt) #could use np here
    
    agent.optimizer.zero_grad()
    pg = torch.stack(pg).sum()
    pg.backward()
    agent.optimizer.step()

# ==============================================================

MAX_EPISODES = 1
BATCH_SIZE = 32
GAMMA = 0.99

env = QuadrupedEnv()
actor = Actor()
critic = Critic()
buff = ReplayBuffer(MAX_EPISODES)

training = True

for episode in range(MAX_EPISODES):
    obs = env.reset()
    obs = torch.Tensor(obs)
    cur_state = obs

    while True: 
        loss = 0

        action = actor(obs)
        # should add OU noise for each action for exploration
        obs, reward, done = env.step(action=action)
        
        # should add replay buffer for random sampling of critic
        new_state = torch.Tensor(obs)
        buff.add(cur_state, action, reward, new_state, done)
        
        batch = buff.get_batch(BATCH_SIZE)
        states = [x[0] for x in batch]
        actions = [x[1] for x in batch]
        rewards = [x[2] for x in batch]
        new_states = [x[3] for x in batch]
        dones = [x[4] for x in batch]
        new_q_batch = []

        # pass new_states, and actor prediction from new_states, should be the target critic network
        target_q_values = critic(new_states, actor(new_states))

        for i in range(len(batch)):
            if dones[i]:
                new_q_batch.append(rewards[i])
            else:
                new_q_batch.append(reward[i] + GAMMA*new_q_batch[i])
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
