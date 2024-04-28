import gymnasium as gym
import numpy as np
import pybullet as p

from gymnasium import spaces

class QuadrupedEnv(gym.Env):

    def __init__(self, render_mode=None):
        self.init_pybullet()

    def init_pybullet(self):
        p.connect(p.DIRECT)
        p.resetSimulation()
        p.setGravity(0, 0, -9.81)
        p.loadURDF("plane.urdf")
        p.resetDebugVisualizerCamera(cameraDistance=0.2, cameraYaw=-60, cameraPitch=-35, cameraTargetPosition=[-0.1,0,0])

        startPos = [0,0,0]
        startOrientation = p.getQuaternionFromEuler([0,0,0])
        robot = p.loadURDF("/model/robot.urdf",startPos, startOrientation)

        mode = p.POSITION_CONTROL
        pos_array = [0, 2, 3, 4, 5, 6, 8, 9 ,10, 12, 13, 14]
        lower_lims = [p.getJointInfo(robot, x)[8] for x in pos_array]
        upper_lims = [p.getJointInfo(robot, x)[9] for x in pos_array]

    def reset(self):
        p.disconnect()
    
    def step(self, action):
