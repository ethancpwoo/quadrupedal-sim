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

p.resetDebugVisualizerCamera(cameraDistance=0.2, cameraYaw=60, cameraPitch=-35, cameraTargetPosition=[0.1,0.05,0])

mode = p.POSITION_CONTROL
pos_array = [0, 1, 2, 4, 5, 6, 8, 9 ,10, 12, 13, 14]
extended = 0
contract = 1.0472

p.setJointMotorControlArray(robot, pos_array, controlMode=mode)

p.changeDynamics(robot, 3, lateralFriction=2, spinningFriction=2)
move = extended
counter = 0

for i in range(10000):
    if move == extended and counter == 100:
         move = contract
         counter = 0
    elif move == contract and counter == 100:
         move = extended
         counter = 0
    p.stepSimulation()
    p.setJointMotorControl2(robot, 3, controlMode=mode, targetPosition=move)
    time.sleep(1./240.)
    counter += 1

chassisPos, chassisOrn = p.getBasePositionAndOrientation(robot)
p.disconnect()
