import gymnasium as gym
import numpy as np
import pybullet as p
import pybullet_data
import time

from gymnasium import spaces

class QuadrupedEnv(gym.Env):

    def __init__(self, render_mode=None):
        self.init_pybullet()
        self.step_count = 0 #initialize for stepping the training
        self.done = False
        self.observation_space = spaces.Dict(
            {
                "velocity": spaces.Box(dtype=np.float32, low=-100, high=100),
                "position": spaces.Box(dtype=np.float32, low=-100, high=100),
                "RPY": spaces.Box(shape=(3,), dtype=np.float32, low=-100, high=100)
            }
        )

        self.action_space = spaces.Box(shape=(12,), dtype=np.float32, low=-100, high=100)

    def init_pybullet(self):
        p.connect(p.DIRECT)
        p.resetSimulation()
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.81)
        p.loadURDF("plane.urdf")
        p.resetDebugVisualizerCamera(cameraDistance=0.2, cameraYaw=-60, cameraPitch=-35, cameraTargetPosition=[-0.1,0,0])

        startPos = [0, 0, 0.0585]
        startOrientation = p.getQuaternionFromEuler([0,0,0])
        self.robot = p.loadURDF("../robot/robot.urdf", startPos, startOrientation)

        self.mode = p.POSITION_CONTROL
        self.pos_array = [0, 2, 3, 4, 5, 6, 8, 9 ,10, 12, 13, 14]
        self.lower_lims = [p.getJointInfo(self.robot, x)[8] for x in self.pos_array]
        self.upper_lims = [p.getJointInfo(self.robot, x)[9] for x in self.pos_array]

        self.start_state = p.saveState()
    
    def _get_obs(self):

        obs = np.array([])
        state = p.getLinkStates(self.robot, self.pos_array)
        for i in range(len(self.pos_array)):
            obs = np.append(obs, np.array(state[i][2]).flatten())
            obs = np.append(obs, np.array(p.getEulerFromQuaternion(state[i][3])).flatten())

        obs = np.append(obs, p.getEulerFromQuaternion(p.getBasePositionAndOrientation(self.robot)[1]))
        obs = obs.flatten()

        return obs

    def reset(self):
        p.restoreState(stateId=self.start_state)
        self.step_count = 0
        self.done = False
        observation = self._get_obs()
        return observation
    
    def step(self, action):
        initPos = p.getBasePositionAndOrientation(self.robot)
        init_ypos = initPos[0][1]

        print(action)
        print(self.pos_array)

        p.setJointMotorControlArray(self.robot, self.pos_array, self.mode, action)

        for i in range(60):
            p.stepSimulation()
            time.sleep(1./240.)

        velocity = p.getBaseVelocity(self.robot)[0][1]
        deltaPos = p.getBasePositionAndOrientation(self.robot)

        delta_ypos = deltaPos[0][1]
        diff = abs(delta_ypos - init_ypos)

        rotations = np.array(deltaPos[1])
        
        reward = 0.05 if velocity > 0.1 else 0
        reward += 0.05 if diff > 0.05 else 0
        reward += -0.01 if np.any(rotations > 0.1) or np.any(rotations < 0.1) else 0

        self.step_count += 1

        if self.step_count == 40:
            self.done = True

        observation = self._get_obs()

        return observation, reward, self.done

