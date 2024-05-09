import numpy as np
import pybullet as p
import pybullet_data
import torch

from quadruped_env import QuadrupedEnv
from models.actor import Actor

def eval():
    device = "cuda:0" if torch.cuda.is_available() else 'cpu'
    agent = Actor().to(device)
    agent.load_state_dict(torch.load('./saved_models/actor_target.pt'))
    env = QuadrupedEnv(render_mode='GUI')
    obs = env.reset()

    #print(np.shape(obs))

    obs = torch.Tensor(obs).cuda()
    action = agent(obs)
    action = action.cpu().detach().numpy()

    for i in range(40):
        new_obs, reward, done = env.step(action)
        print(f'reward: {reward}')
        obs = torch.Tensor(new_obs).cuda()
        action = agent(obs)
        action = action.cpu().detach().numpy()

    p.disconnect()

if __name__ == '__main__': 
    eval()