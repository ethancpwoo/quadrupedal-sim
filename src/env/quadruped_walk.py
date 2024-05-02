import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from quadruped_env import QuadrupedEnv
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

        self.fc1 = nn.Linear(75, 225)
        self.fc2 = nn.Linear(225, 115)
        self.probs = nn.Linear(115, 12)
        self.optimizer = torch.optim.AdamW(self.parameters(), lr=learning_rate)
    
    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.probs(x)

        return F.softmax(x, dim=0)
    
    def get_action(self, observation):
        obs = torch.from_numpy(observation)
        obs = obs.to(torch.float32)
        probs = self.forward(obs)

        highest_probability_action = np.random.choice([x for x in range(12)], p=probs.detach().numpy())
        log_prob = torch.log(probs.squeeze(0)[highest_probability_action])

        return highest_probability_action, log_prob

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
agent = Agent()

max_episodes = 1

obs = env.reset()
training = True

for episode in range(max_episodes):
    obs = env.reset()
    log_probs = []
    rewards = []

    while True: 
        action, log_prob = agent.get_action(obs)
        obs, reward, done = env.step(action=action)
        log_probs.append(log_prob)
        rewards.append(reward)
        state = obs

        if done: 
            update_agent(agent, rewards, log_probs)
            break        

print("done")
