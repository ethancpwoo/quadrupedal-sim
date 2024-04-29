import gymnasium as gym
import numpy as np
import pybullet as p
import time

from gymnasium import spaces

class QuadrupedEnv(gym.Env):

    def __init__(self, render_mode=None):
        self.init_pybullet()
        self.observations = []
        self.step_count = 0 #initialize for stepping the training
        self.done = False
        self.observation_space = spaces.Dict(
            {
                "velocity": spaces.Box(dtype=np.float32),
                "position": spaces.Box(dtype=np.float32),
                "RPY": spaces.Box(shape=(3,), dtype=np.float32)
            }
        )

        self.action_space = spaces.Box(shape=(12,), dtype=np.float32)

    def init_pybullet(self):
        p.connect(p.DIRECT)
        p.resetSimulation()
        p.setGravity(0, 0, -9.81)
        p.loadURDF("plane.urdf")
        p.resetDebugVisualizerCamera(cameraDistance=0.2, cameraYaw=-60, cameraPitch=-35, cameraTargetPosition=[-0.1,0,0])

        startPos = [0, 0, 0.0585]
        startOrientation = p.getQuaternionFromEuler([0,0,0])
        self.robot = p.loadURDF("/robot/robot.urdf", startPos, startOrientation)

        self.mode = p.POSITION_CONTROL
        self.pos_array = [0, 2, 3, 4, 5, 6, 8, 9 ,10, 12, 13, 14]
        self.lower_lims = [p.getJointInfo(self.robot, x)[8] for x in self.pos_array]
        self.upper_lims = [p.getJointInfo(self.robot, x)[9] for x in self.pos_array]
    
    def reset(self):
        p.disconnect()
        self.step_count = 0
        self.done = False
        
        for i in self.pos_array:
            self.observations.append(np.array(p.getLinkStates()[i][2]).flatten)

    
    def step(self, action):
        initPos = p.getBasePositionAndOrientation(self.robot)
        init_ypos = initPos[0][1]

        p.setJointMotorControlArray(self.robot, self.pos_array, self.mode, action)

        for i in range(60):
            p.stepSimulation()
            time.sleep(1./240.)

        velocity = p.getBaseVelocity(self.robot)[0][1]
        deltaPos = p.getBasePositionAndOrientation(self.robot)

        delta_ypos = deltaPos[0][1]
        diff = abs(delta_ypos - init_ypos)

        rotations = np.array(abs(deltaPos[1]))
        
        reward = 0.05 if velocity > 0.1 else 0
        reward += 0.05 if diff > 0.05 else 0
        reward += -0.01 if np.any(rotations > 0.1) else 0

        self.step_count += 1

        if self.step_count == 40:
            self.done = True

        return reward, self.done

