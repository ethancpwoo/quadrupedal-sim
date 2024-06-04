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

        self.fc1 = nn.Linear(17, 250)
        self.fc2 = nn.Linear(250, 75)
        self.legs = nn.Linear(75, 8)
        self.learning_rate = 1e-4
        self.optimizer = torch.optim.AdamW(self.parameters(), lr=self.learning_rate)
    
    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        # print(x)
        legs = self.legs(x)
        legs = F.tanh(legs)
        # print(legs)
        # print(hips)
        return legs