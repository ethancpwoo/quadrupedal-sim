import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from env.quadruped_env import QuadrupedEnv
from tqdm import tqdm


device = 'cuda' if torch.cuda.is_available() else 'cpu'
learning_rate = 3e-4
gamma = 0.9

class Agent(nn.Module):
    """
    Define multi-layer perceptron to deep learn and optimize policy.
    """
    def __init__(self):
        super(Agent, self).__init__()

        self.fc1 = nn.Linear(75, 450)
        self.fc2 = nn.Linear(450, 300)
        self.fc3 = nn.Linear(300, 60)
        self.probs = nn.Linear(60, 12)
        self.optimizer = torch.optim.AdamW(self.parameters(), lr=learning_rate)
    
    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.relu(x)
        x = self.probs(x)

        return F.softmax(x, dim=1)

def update_agent(agent, rewards, log_probs):
    drs = []

    for i in range(len(rewards)):
        total = 0
        pw = 0
        for reward in rewards[i:]:
            total += gamma**pw * reward
            pw += 1
        drs.append(total)
    
    drs = torch.tensor(drs)
    drs = (drs - drs.mean()) #normalize them

    pg = []
    for log_prob, gt in zip(log_probs, drs):
        pg.append(-log_prob * gt)
    
    agent.optimizer.zero_grad()
    pg = torch.stack(pg).sum()
    pg.backward()
    agent.optimizer.step()

env = QuadrupedEnv()
obs = env.reset()
training = True
agent = Agent()

while training:
