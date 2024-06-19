import numpy as np
import os
import pybullet as p
import pybullet_data
import rclpy
import torch

from action_state.action import Jointstate
from .saved_models.actor import Actor
from rclpy.action import ActionServer
from rclpy.node import Node

class ModelAction(Node):
    
    def __init__(self):
        super().__init__('model_action')
        self._action_server = ActionServer(self, Jointstate, 'jointstate', self.execute_callback)
        self.device = device = "cuda:0" if torch.cuda.is_available() else 'cpu'
        self.actor = Actor().to(device)
        model = os.path.join(os.path.dirname(__file__), 'saved_models', 'actor_target.pt')
        self.actor.load_state_dict(torch.load(model, map_location=torch.device('cpu')))
        self.mode = p.POSITION_CONTROL

        p.connect(p.DIRECT)
        p.resetSimulation()
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.81)
        p.loadURDF("plane.urdf")
        startPos = [0, -0.061531337528119075, 0.0585]
        startOrientation = p.getQuaternionFromEuler([0,0,0])
        robot_file = os.path.join(os.path.dirname(__file__), 'robot', 'robot.urdf')
        self.robot = p.loadURDF(robot_file, startPos, startOrientation)
        self.pos_array = [1, 2, 5, 6, 9, 10, 13, 14]        
        p.setJointMotorControlArray(self.robot, self.pos_array, self.mode)
        p.setJointMotorControlArray(self.robot, [0, 4, 8, 12], self.mode, [0, 0, 0, 0])

        self.lower_lims = [p.getJointInfo(self.robot, x)[8] for x in self.pos_array]
        self.upper_lims = [p.getJointInfo(self.robot, x)[9] for x in self.pos_array]
        
        for i in range(1000):
            p.stepSimulation()

        self.start_state = p.saveState()

    def normalize_obs(self, obs, max, min):
        normal_vals = []
        for observation in obs:
            normal_vals.append(2 * ((observation - min)/(max - min)) - 1)
        return normal_vals

    def _get_obs(self):
        obs = np.array([])
        joint_state = p.getJointStates(self.robot, self.pos_array)
        base_state = p.getBasePositionAndOrientation(self.robot)
        velocity_state = p.getBaseVelocity(self.robot)

        for i in range(len(self.pos_array)):
            obs = np.append(obs, self.normalize_obs(np.array(round(joint_state[i][0], 5)).flatten(), self.upper_lims[i], self.lower_lims[i])) # joint pos

        obs = np.append(obs, self.normalize_obs(p.getEulerFromQuaternion(base_state[1]), 0.1745, -0.1745)) # base rotation
        obs = np.append(obs, self.normalize_obs(np.array(velocity_state[0]).flatten(), 0.06, -0.06)) # base velocity
        obs = np.append(obs, self.normalize_obs(np.array(velocity_state[1]).flatten(), 1.5, -1.5)) # base ang velocity
        obs = obs.flatten()
        # print(obs)
        return obs

    def run_model(self):
        obs = self._get_obs()
        obs = torch.Tensor(obs)
        action = self.actor.forward(obs)

        for i in range(4):
            action[i] = action[i] * 1.0472
            action[i + 4] = action[i + 4] * -1.0472
        
        p.setJointMotorControlArray(self.robot, self.pos_array, self.mode, action)

        for i in range(24):
            p.stepSimulation()
        
        action = action.tolist()

        print(type(action))
        for item in action:
            print(type(item))

        return action
    
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        result_msg = Jointstate.Result()

        result = self.run_model()
        result_msg.jointactions = result
        print(result)
        goal_handle.succeed()
        return result_msg
    

def main(args=None):
    rclpy.init(args=args)
    model_action = ModelAction()
    rclpy.spin(model_action)

if __name__ == '__main__': 
    main()