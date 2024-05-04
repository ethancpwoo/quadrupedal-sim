import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class Critic(nn.Module):
    """
    Define DQN critic 
    """
    def __init__(self):
        super(Critic, self).__init__()
        self.fc_states = nn.Linear(75, 225)
        self.fc_actions = nn.Linear(12, 115)

        self.fc2_states = nn.Linear(225, 115)
        
        self.fc_all = nn.Linear(115, 115)
        self.actions = nn.Linear(115, 12)
        self.learning_rate = 3e-4
        self.optimizer = torch.optim.AdamW(self.parameters(), lr=self.learning_rate)
        self.loss = nn.CrossEntropyLoss()
    
    def forward(self, states, actions):
        states = self.fc_states(states)
        actions = self.fc_actions(actions)
        
        states = F.relu(states)
        states = self.fc2_states(states)

        x = torch.add(states, actions)
        x = self.fc_all(x)
        x = F.relu(states)
        x = self.actions(x)

        return x
    
    def train(self, q_values, reward):
        self.zero_grad()
        loss = self.loss(q_values, reward)
        loss.backward()
        self.optimizer.step()

    # implement target
