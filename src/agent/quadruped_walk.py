import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from env.quadruped_env import QuadrupedEnv
from tqdm import tqdm


device = 'cuda' if torch.cuda.is_available() else 'cpu'
learning_rate = 3e-4

class Agent(nn.Module):
    """
    Define multi-layer perceptron to deep learn and optimize policy.
    """
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(75, 450)
        self.fc2 = nn.Linear(450, 300)
        self.fc3 = nn.Linear(300, 60)
        self.probs = nn.Linear(60, 12)
    
    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.relu(x)
        x = self.probs(x)

        return F.softmax(x, dim=1)

env = QuadrupedEnv()
obs = env.reset()
training = True
agent = Agent()
optimizer = torch.optim.AdamW(agent.parameters(), lr=learning_rate)

while training:
