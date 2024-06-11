import numpy as np
import pybullet as bullet
import pybullet_data
import time

def main():

    #boilerplate code for pybullet
    bullet.connect(bullet.GUI)
    bullet.resetSimulation()
    bullet.setAdditionalSearchPath(pybullet_data.getDataPath())
    bullet.setGravity(0, 0, -9.8)
    bullet.setRealTimeSimulation(0)

    # load urdf and assets
    bullet.loadURDF("plane.urdf", [0, 0, 0], [0, 0, 0, 1])
    target_id = bullet.loadURDF("model/robot.urdf", [0, 0, 3], [0, 0, 0, 1])

    numJoints = bullet.getNumJoints(target_id)
    print(numJoints)
    for i in range(numJoints):
        print(bullet.getJointInfo(target_id, i))

    for step in range(300):
        focus_position, _ = bullet.getBasePositionAndOrientation(target_id)
        bullet.resetDebugVisualizerCamera(cameraDistance = 0.2, cameraYaw = 0, cameraPitch = -40, cameraTargetPosition = focus_position)
        bullet.stepSimulation()
        time.sleep(0.01)


if __name__ == '__main__':
    main()