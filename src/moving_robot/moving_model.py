import numpy as np
import pybullet as p
import time
import pybullet_data

from enum import Enum

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-9.81)

planeId = p.loadURDF("plane.urdf")
startPos = [0.0, 0, 0.0585]
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
robot = p.loadURDF("../robot/robot.urdf", startPos, startOrientation)

numJoints = p.getNumJoints(robot)
print(numJoints) 
for i in range(numJoints):
    print(p.getJointInfo(robot, i))

# cam = p.getDebugVisualizerCamera()
# print(cam[8])
# print(cam[9])
# print(cam[10])

p.resetDebugVisualizerCamera(cameraDistance=0.2, cameraYaw=-60, cameraPitch=-35, cameraTargetPosition=[-0.1,0,0])

mode = p.VELOCITY_CONTROL
pos_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
thighs = [1, 5, 9, 13]
foots = [2, 6, 9, 14]
lower_lims = [p.getJointInfo(robot, x)[8] for x in pos_array]
upper_lims = [p.getJointInfo(robot, x)[9] for x in pos_array]
flexed = [1.0472 for x in range(len(pos_array))]
relaxed = [-1.0472 for x in range(len(pos_array))]

# hips [-0.261799, 0.261799]
# left [0, 1.0472]
# right [-1.0472, 0]

extended = [0, 1.0472, 0, 0, 1.0472, 0, 0, -1.0472, 0, 0, -1.0472, 0]
tweaking = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
torque = [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(len(pos_array)):
#     tweaking.append(np.random.uniform(lower_lims[i], upper_lims[i]))

def check_lims():
    joint_states = [p.getJointState(robot, x)[0] for x in pos_array]
    print(joint_states[1])
    # Adjust target velocity based on positional limits
    for j, i in enumerate(joint_states[0:4]):
        if i < 0:
            p.setJointMotorControl2(robot, pos_array[j], mode, targetVelocity=0)
        elif i > 1.0472:
            p.setJointMotorControl2(robot, pos_array[j], mode, targetVelocity=0)

    for j, i in enumerate(joint_states[4:8]):
        if i > 0:
            p.setJointMotorControl2(robot, pos_array[j + 4], mode, targetVelocity=0)
        elif i < -1.0472:
            p.setJointMotorControl2(robot, pos_array[j + 4], mode, targetVelocity=0)


#set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
p.setJointMotorControlArray(robot, pos_array, mode, targetVelocities=tweaking)
for i in range(100):
    # tweaking = []
    # for i in range(len(pos_array)):
    #     tweaking.append(np.random.uniform(lower_lims[i], upper_lims[i]))
    
    p.stepSimulation()
    # print(p.getBasePositionAndOrientation(robot)[0])
    #print(p.getJointStates(robot, pos_array))
    # velocity = p.getBaseVelocity(robot)[0][1]
    # print(velocity)
    # print(p.getEulerFromQuaternion(p.getBasePositionAndOrientation(robot)[1]))
    pos = p.getBasePositionAndOrientation(robot)
    rotations = np.array(p.getEulerFromQuaternion(pos[1])) 
    # print(rotations)
    # links = []
    # for i in range(12):
    #     rel_pos = p.getLinkStates(robot, pos_array)[i][2]
    #     links.append(rel_pos)
    time.sleep(1./240.)
contacts = p.getContactPoints(robot, planeId, 2)
# thigh_pos = [p.getLinkStates(robot, [2, 5, 8, 11])[x][0][2] for x in range(4)] 
# print(thigh_pos)
print(contacts)
print()
print()

p.setJointMotorControlArray(robot, pos_array, mode, targetVelocities=torque)
for i in range(1000):
    check_lims()
    p.stepSimulation()
    time.sleep(1./240.)

contacts = p.getContactPoints(robot, planeId, 2)
# thigh_pos = [p.getLinkStates(robot, [2, 5, 8, 11])[x][0][2] for x in range(4)] 
# print(thigh_pos)
print(contacts)

# links = np.array(links)
#print(links.flatten())
chassisPos, chassisOrn = p.getBasePositionAndOrientation(robot)
#print(chassisPos,chassisOrn)
p.disconnect()
