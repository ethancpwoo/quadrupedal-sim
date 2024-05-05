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
startOrientation = p.getQuaternionFromEuler([0,0,0])
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

mode = p.POSITION_CONTROL
pos_array = [0, 2, 3, 4, 5, 6, 8, 9 ,10, 12, 13, 14]
lower_lims = [p.getJointInfo(robot, x)[8] for x in pos_array]
upper_lims = [p.getJointInfo(robot, x)[9] for x in pos_array]
flexed = [1.0472 for x in range(len(pos_array))]
relaxed = [-1.0472 for x in range(len(pos_array))]

tweaking = []
for i in range(len(pos_array)):
    tweaking.append(np.random.uniform(lower_lims[i], upper_lims[i]))

#set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
p.setJointMotorControlArray(robot, pos_array, controlMode=mode, targetPositions=tweaking)
for i in range(1):
    # tweaking = []
    # for i in range(len(pos_array)):
    #     tweaking.append(np.random.uniform(lower_lims[i], upper_lims[i]))
    
    p.stepSimulation()
    #print(p.getEulerFromQuaternion(p.getBasePositionAndOrientation(robot)[1]))
    #print(p.getBaseVelocity(robot)[0][0])
    links = []
    for i in range(12):
        rel_pos = p.getLinkStates(robot, pos_array)[i][2]
        links.append(rel_pos)
    time.sleep(1./240.)

links = np.array(links)
print(links.flatten())
chassisPos, chassisOrn = p.getBasePositionAndOrientation(robot)
#print(chassisPos,chassisOrn)
p.disconnect()
