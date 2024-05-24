import numpy as np
import pybullet as p
import pybullet_data
import time

from utils.ornstienUhlenbeck import OU

"""
TODO:
    Create stack post if cannot solve by next week.
    1) Normalize inputs to -1 to 1
    2) Change reward such that must pass certain threshold to gain reward, else scaled negative
    3) Try PyTorch DDPG, make QuadrupedEnv inherit Gym
    4) Implement PPO or go to stack post...
"""        
class QuadrupedEnv():

    def __init__(self, render_mode):
        self.orn_uhlen = OU()
        
        # Graphing data init
        self.episode_displacement_reward = 0
        self.episode_time_reward = 0
        self.episode_height_reward = 0
        self.episode_rotations_reward = 0

        self.final_positions = []
        self.final_times = []
        self.reward_time = []
        self.reward_vel = []
        self.reward_height =  []
        self.reward_rotations = []

        # Step counting
        self.last_pos = 0
        self.step_count = 0
        self.last_pos = 0
        self.total_steps = 150
        # Initialize for stepping the training

        self.render_mode = render_mode
        self.done = False
        
        self.init_pybullet()

    def init_pybullet(self):
        if self.render_mode == 'GUI':
            p.connect(p.GUI) # p.GUI for graphical
        else:
            p.connect(p.DIRECT)

        p.resetSimulation()
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.81)
        p.loadURDF("plane.urdf")
        p.resetDebugVisualizerCamera(cameraDistance=0.2, cameraYaw=-90, cameraPitch=-35, cameraTargetPosition=[-0.1,0,0])

        startPos = [0, -0.061531337528119075, 0.0585]
        startOrientation = p.getQuaternionFromEuler([0,0,0])
        self.robot = p.loadURDF("../robot/robot.urdf", startPos, startOrientation)

        self.mode = p.POSITION_CONTROL
        self.pos_array = [1, 2, 4, 5, 7, 8, 10, 11, 0, 3, 6, 9]
        self.lower_lims = [p.getJointInfo(self.robot, x)[8] for x in self.pos_array]
        self.upper_lims = [p.getJointInfo(self.robot, x)[9] for x in self.pos_array]

        for i in self.pos_array:
            p.changeDynamics(self.robot, i, lateralFriction=10, spinningFriction=10)

        p.setJointMotorControlArray(self.robot, self.pos_array, self.mode)

        for i in range(1000):
            p.stepSimulation()

        self.start_state = p.saveState()
    
    def _get_obs(self):
        obs = np.array([])
        joint_state = p.getJointStates(self.robot, self.pos_array)
        base_state = p.getBasePositionAndOrientation(self.robot)
        velocity_state = p.getBaseVelocity(self.robot)

        for i in range(len(self.pos_array)):
            obs = np.append(obs, np.array(joint_state[i][0]).flatten()) # joint pos
            # obs = np.append(obs, np.array(joint_state[i][1]).flatten()) # joint velocities

        obs = np.append(obs, p.getEulerFromQuaternion(base_state[1])) # base rotation
        obs = np.append(obs, np.array(velocity_state[0]).flatten()) # base velocity
        obs = np.append(obs, np.array(velocity_state[1]).flatten()) # base ang velocity
        obs = obs.flatten()

        return obs

    def reset(self):
        p.restoreState(stateId=self.start_state)
        self.step_count = 0
        self.done = False
        return self._get_obs()
    
    def step(self, action, epsilon):
        print(action)
        action[0:4] = np.clip(action[0:4] + np.array([max(epsilon, 0) * self.orn_uhlen.OU(action[x], 0.5, 0.75, 0.5) for x in range(4)]).flatten(), 0, 1)
        action[4:8] = np.clip(action[4:8] + np.array([max(epsilon, 0) * self.orn_uhlen.OU(action[x], 0.5, 0.75, 0.5) for x in range(4)]).flatten(), 0, 1)
        action[8:12] = np.clip(action[8:12] + np.array([max(epsilon, 0) * self.orn_uhlen.OU(action[x], 0, 1, 0.05) for x in range(4)]).flatten(), -1, 1)
        action_train = action
        # Left side
        for i in range(4):
            action[i] = action[i] * 1.0472 

        # Right side
        for i in range(4):
            action[i + 4] = action[i + 4] * -1.0472
        
        # Hips
        for i in range(4):
            action[i + 8] = action[i + 8] * 0.261799

        p.setJointMotorControlArray(self.robot, self.pos_array, self.mode, action)

        for i in range(24):
            p.stepSimulation()
            if self.render_mode == 'GUI':
                time.sleep(1/240)

        pos = p.getBasePositionAndOrientation(self.robot)
        rotations = np.array(p.getEulerFromQuaternion(pos[1]))       
        
        # Reward function
        reward = 0
        reward_time = 0
        reward_displacement = 0
        # if(self.step_count > 148):
        #     reward_time = (self.step_count/self.total_steps)
        displacement = pos[0][1] - self.last_pos
        # if abs(displacement) < 0.005 :
        #     reward_displacement = -1
        # else:
        #     reward_displacement = (-75 * displacement)
        reward_displacement = (-120 * displacement)
        reward_time += (self.step_count/self.total_steps)
        reward_height = np.sqrt(np.square(0.0522 - pos[0][2]))
        reward_rotation = abs(rotations[2] + rotations[1] + rotations[0]) * 0.1
        reward = reward_time + reward_displacement - reward_height - reward_rotation

        # - reward_height - reward_rotation
        # Graphing/Debugging purposes
        self.episode_displacement_reward += reward_displacement
        self.episode_time_reward += reward_time
        self.episode_height_reward -= reward_height
        self.episode_rotations_reward -= reward_rotation

        self.step_count += 1
        self.last_pos = pos[0][1]

        # Episode ending
        if self.step_count == self.total_steps or pos[0][2] < 0.0455 or abs(rotations[0]) > 0.1745 or abs(rotations[1]) > 0.1745 or abs(rotations[2]) > 0.3491:
            self.final_positions.append(pos[0][1])
            self.final_times.append(self.step_count)
            self.reward_vel.append(self.episode_displacement_reward)
            self.reward_time.append(self.episode_time_reward)
            self.reward_height.append(self.episode_height_reward)
            self.reward_rotations.append(self.episode_rotations_reward)

            self.episode_displacement_reward = 0
            self.episode_time_reward = 0
            self.episode_height_reward = 0
            self.episode_rotations_reward = 0

            self.done = True

        observation = self._get_obs()

        return action_train, observation, reward, self.done

