import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class Actor(nn.Module):
    """
    Define multi-layer perceptron to deep learn and optimize policy.
    """
    def __init__(self):
        super(Actor, self).__init__()

        self.fc1 = nn.Linear(33, 450)
        self.fc2 = nn.Linear(450, 300)
        self.actions = nn.Linear(300, 12)
        self.learning_rate = 1e-3
        self.optimizer = torch.optim.AdamW(self.parameters(), lr=self.learning_rate)
    
    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.actions(x)

        return F.tanh(x)

    def train(self, critic_out):
        self.zero_grad()
        critic_grad = critic_out.mean()
        critic_grad.backward()
        self.optimizer.step()
        return critic_grad

    # implement target