import numpy as np
import pybullet as p
import pybullet_data
import rclpy
import torch

from actor import Actor
from rclpy.node import Node

class ModelAction(Node):
    
    def init(self):
        super().__init__('model_action')

    # def eval():
    #     device = "cuda:0" if torch.cuda.is_available() else 'cpu'
    #     agent = Actor().to(device)
    #     agent.load_state_dict(torch.load('./saved_models/actor_target.pt'))

    #     obs = torch.Tensor(obs).cuda()
    #     action = agent.forward(obs)
    #     action = action.cpu().detach().numpy()

    #     for i in range(40):
                
    #         action, new_obs, reward, done = env.step(action, 0)

    #         if done:
    #             break
    #         print(f'reward: {reward}')
    #         obs = torch.Tensor(new_obs).cuda()
    #         action = agent(obs)
    #         action = action.cpu().detach().numpy()

        p.disconnect()

def main(args=None):
    rclpy.init(args=args)
    model_action = ModelAction()
    rclpy.spin(model_action)
    model_action.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__': 
    main()
