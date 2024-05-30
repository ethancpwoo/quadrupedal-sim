import numpy as np
import pybullet as p
import pybullet_data
import time

from utils.ornstienUhlenbeck import OU

"""
TODO:
    1) Make feet DOF deterministic 1 or 0, adjust with rotating thighs.
    2) If that doesnt work, go back into cad and make balled feet. 
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
        self.total_steps = 250
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
        self.left_side = [1, 4, 2, 5]
        self.right_side = [7, 10, 8, 11]
        self.pos_array = [1, 4, 2, 5, 7, 10, 8, 11]
        self.lower_lims = [p.getJointInfo(self.robot, x)[8] for x in self.pos_array]
        self.upper_lims = [p.getJointInfo(self.robot, x)[9] for x in self.pos_array]

        for i in self.pos_array:
            p.changeDynamics(self.robot, i, lateralFriction=2, spinningFriction=2)

        p.setJointMotorControlArray(self.robot, self.pos_array, self.mode)

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

    def reset(self):
        p.restoreState(stateId=self.start_state)
        self.step_count = 0
        self.done = False
        return self._get_obs()
    
    def step(self, action, epsilon):
        # print(action)
        action[0:2] = np.clip(action[0:2] + np.array([max(epsilon, 0) * self.orn_uhlen.OU(action[x], 0.5, 0.2, 0.8) for x in range(2)]).flatten(), 0, 1)
        action[2:4] = np.clip(action[2:4] + np.array([max(epsilon, 0) * self.orn_uhlen.OU(action[x], 0.6, 0.5, 0.4) for x in range(2)]).flatten(), 0, 1)
        action[4:6] = np.clip(action[4:6] + np.array([max(epsilon, 0) * self.orn_uhlen.OU(action[x], 0.5, 0.2, 0.8) for x in range(2)]).flatten(), 0, 1)
        action[6:8] = np.clip(action[6:8] + np.array([max(epsilon, 0) * self.orn_uhlen.OU(action[x], 0.6, 0.5, 0.4) for x in range(2)]).flatten(), 0, 1)
        action_train = action
        # Left side
        for i in range(4):
            action[i] = action[i] * 1.0472 

        # Right side
        for i in range(4):
            action[i + 4] = action[i + 4] * -1.0472

        p.setJointMotorControlArray(self.robot, self.pos_array, self.mode, action)

        for i in range(20):
            p.stepSimulation()
            if self.render_mode == 'GUI':
                time.sleep(1/240)

        pos = p.getBasePositionAndOrientation(self.robot)
        rotations = np.array(p.getEulerFromQuaternion(pos[1]))       
        thigh_pos = [p.getLinkStates(self.robot, [1, 4, 7, 10])[x][0][2] for x in range(4)]
        diff_pos = [np.sqrt(np.square(p.getLinkStates(self.robot, [1, 4, 7, 10])[x][0][2] - 0.475)) for x in range(4)]
        thigh_end = [p.getLinkStates(self.robot, [1, 4, 7, 10])[x][0][2] < 0.035 for x in range(4)]
        # Reward function
        reward = 0
        reward_time = 0
        reward_displacement = 0
        reward_height = 0
        reward_rotation = 0
        velocity = p.getBaseVelocity(self.robot)[0][1]
        # if(self.step_count > 148):
        #     reward_time = (self.step_count/self.total_steps)
        displacement = pos[0][1] - self.last_pos
        if abs(displacement) > 0.01 :
            reward_displacement = (-150 * displacement)
        else:
            reward_displacement = (-50 * 0.01)
        # reward_displacement = -120 * velocity
        # reward_time += (self.step_count/self.total_steps)
        # reward_height = np.sqrt(np.square(0.0522 - pos[0][2]))
        reward_rotation += abs(rotations[2]) * 0.1
        reward_rotation += abs(rotations[1]) * 0.1 
        reward_height = np.sum(diff_pos) * 75
        reward = reward_time + reward_displacement - reward_height - reward_rotation

        # - reward_height - reward_rotation
        # Graphing/Debugging purposes
        self.episode_displacement_reward += reward_displacement
        # self.episode_time_reward += reward_time
        self.episode_height_reward -= reward_height
        self.episode_rotations_reward -= reward_rotation

        self.step_count += 1
        self.last_pos = pos[0][1]

        # Episode ending
        if (self.step_count == self.total_steps or pos[0][2] < 0.0455 or abs(rotations[0]) > 0.3 or 
            abs(rotations[1]) > 0.2 or abs(rotations[2]) > 0.2 or np.any(thigh_end)):
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

