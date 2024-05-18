import numpy as np
import pybullet as p
import pybullet_data
import time

class QuadrupedEnv():

    def __init__(self, render_mode):
        self.done = False

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

        # self.final_roll = []
        # self.final_pitch = []
        # self.final_yaws = []
        self.render_mode = render_mode
        self.last_pos = 0
        self.step_count = 0
        self.last_pos = 0
        self.total_steps = 150 #initialize for stepping the training
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

        startPos = [0, 0, 0.0585]
        startOrientation = p.getQuaternionFromEuler([0,0,0])
        self.robot = p.loadURDF("../robot/robot.urdf", startPos, startOrientation)

        self.mode = p.POSITION_CONTROL
        self.pos_array = [0, 2, 3, 4, 5, 6, 8, 9 ,10, 12, 13, 14]
        self.lower_lims = [p.getJointInfo(self.robot, x)[8] for x in self.pos_array]
        self.upper_lims = [p.getJointInfo(self.robot, x)[9] for x in self.pos_array]

        for i in self.pos_array:
            p.changeDynamics(self.robot, i, lateralFriction=10, spinningFriction=10)

        self.start_state = p.saveState()
    
    def _get_obs(self):

        obs = np.array([])
        joint_state = p.getJointStates(self.robot, self.pos_array)
        base_state = p.getBasePositionAndOrientation(self.robot)
        velocity_state = p.getBaseVelocity(self.robot)

        for i in range(len(self.pos_array)):
            obs = np.append(obs, np.array(joint_state[i][0]).flatten()) # joint pos
            obs = np.append(obs, np.array(joint_state[i][1]).flatten()) # joint velocities

        obs = np.append(obs, p.getEulerFromQuaternion(base_state[1])) # base rotation
        obs = np.append(obs, np.array(velocity_state[0]).flatten()) # base velocity
        obs = np.append(obs, np.array(velocity_state[1]).flatten()) # base ang velocity
        obs = obs.flatten()

        return obs

    def reset(self):
        p.restoreState(stateId=self.start_state)
        self.step_count = 0
        self.done = False
        observation = self._get_obs()
        return observation
    
    def step(self, action):
        # initPos = p.getBasePositionAndOrientation(self.robot)
        # print(action)

        for i in range(len(self.pos_array)):
            action[i] = np.interp(action[i], (-1, 1), (self.lower_lims[i], self.upper_lims[i]))

        # print(action)

        p.setJointMotorControlArray(self.robot, self.pos_array, self.mode, action)

        for i in range(24):
            p.stepSimulation()
            if self.render_mode == 'GUI':
                time.sleep(1/240)

        pos = p.getBasePositionAndOrientation(self.robot)
        rotations = np.array(p.getEulerFromQuaternion(pos[1]))       
        reward = 0
        
        reward_time = 0
        if(self.step_count == 50):
            reward_time = 10 * (self.step_count/self.total_steps)
        if(self.start_count == 125):
            reward_time = 10 * (self.step_count/self.total_steps)
        reward_displacement = (-20 * (pos[0][1] - self.last_pos))
        reward_height = np.sqrt(np.square(0.0522 - pos[0][2])) * 50
        reward_rotation = rotations[2]
        
        self.episode_displacement_reward += reward_displacement
        self.episode_time_reward += reward_time
        self.episode_height_reward -= reward_height
        self.episode_rotations_reward -= reward_rotation
        reward = reward_time + reward_displacement - reward_height - reward_rotation

        # 0.455 is fallen down, 0.522 is normal. 
        self.step_count += 1
        self.last_pos = pos[0][1]

        if self.step_count == self.total_steps or pos[0][2] < 0.0455 or abs(rotations[0]) > 0.1745 or abs(rotations[1]) > 0.1745 or abs(rotations[2]) > 0.3491:
            self.final_positions.append(pos[0][1])
            self.final_times.append(self.step_count)
            self.reward_vel.append(self.episode_displacement_reward)
            self.reward_time.append(self.episode_time_reward)
            self.reward_height.append(self.episode_height_reward)
            self.reward_rotations.append(self.episode_rotations_reward)
            # self.final_roll.append(rotations[0])
            # self.final_pitch.append(rotations[1])
            # self.final_yaws.append(rotations[2])

            self.episode_displacement_reward = 0
            self.episode_time_reward = 0
            self.episode_height_reward = 0
            self.episode_rotations_reward = 0

            self.done = True

        observation = self._get_obs()

        return observation, reward, self.done

