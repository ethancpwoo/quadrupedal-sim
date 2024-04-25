import pybullet as p
import time
import pybullet_data


physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-9.81)

planeId = p.loadURDF("plane.urdf")
startPos = [0,0,0]
startOrientation = p.getQuaternionFromEuler([0,0,0])
robot = p.loadURDF("/model/robot.urdf",startPos, startOrientation)

# numJoints = p.getNumJoints(robot)
# print(numJoints) 
# for i in range(numJoints):
#     print(p.getJointInfo(robot, i))

mode = p.VELOCITY_CONTROL
cam = p.getDebugVisualizerCamera()
print(cam[8])
print(cam[9])
print(cam[10])
p.resetDebugVisualizerCamera(cameraDistance=0.2, cameraYaw=-60, cameraPitch=-35, cameraTargetPosition=[-0.1,0,0])

#set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
for i in range (1000):
    p.setJointMotorControl2(robot, 1, controlMode=mode, targetVelocity=10)
    p.stepSimulation()
    time.sleep(1./240.)

chassisPos, chassisOrn = p.getBasePositionAndOrientation(robot)
print(chassisPos,chassisOrn)
p.disconnect()
