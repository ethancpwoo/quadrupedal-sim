# quadrupedal-sim

## Overview

Using PyBullet to simulate quadrupedal robotic movement. 

moving_model.py is for testing each joint in the URDF file \

Current implementation does not have mimiced joints nor defined constraints within PyBullet. Thigh and Foot are independent DOFs.

## RL Approach and Method

Reward function will be based on the position of the chassis. Unlike the Solo12 or other high level quadrupeds using joint-independent reward functions, this quadruped will use the chassis' RPY + velocity.

## Running

```shell
cd /src/
python moving_model.py
```