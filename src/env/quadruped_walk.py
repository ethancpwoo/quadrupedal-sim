import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from actor import Actor
from critic import Critic
from quadruped_env import QuadrupedEnv
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

env = QuadrupedEnv()
actor = Actor()
critic = Critic()

max_episodes = 1

training = True

for episode in range(max_episodes):
    obs = env.reset()

    while True: 
        loss = 0

        action = actor(obs)
        # should add OU noise for each action for exploration

        obs, reward, done = env.step(action=action)
        # should add replay buffer for random sampling of critic

        q_values = critic.forward(obs, actor(obs))
        
        # for i in range batch size

        if training:
            critic.train(q_values, reward)

            critic_out = -critic(obs, actor(obs))
            actor.train(critic_out)

            # weights into targets

        if done: 
            break        

print("done")
