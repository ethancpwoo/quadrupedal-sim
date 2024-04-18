import numpy as np
import pybullet as bullet
import pybullet_data
import time

def main():
    bullet.connect(bullet.GUI)
    bullet.resetSimulation()
    bullet.setAdditionalSearchPath(pybullet_data.getDataPath())
    bullet.setGravity(0, 0, -9.8)
    bullet.setRealTimeSimulation(0)
    time.sleep(10)

if __name__ == '__main__':
    main()