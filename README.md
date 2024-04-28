# quadrupedal-sim

## Overview

Using PyBullet to simulate quadrupedal robotic movement. 

moving_model.py is for testing each joint in the URDF file \

Current implementation does not have mimiced joints nor defined constraints within PyBullet. Thigh and Foot are independent DOFs.

## RL Approach and Method

Reward function will be based on the position of the chassis. Unlike the Solo12 or other high level quadrupeds using joint-independent reward functions, this quadruped will use the chassis' RPY + velocity.

Model-Free learning, using Policy Gradient for direct optimazation of walking the quadruped. Stochastic Policy to capture uncertainty of realistic walking.

Based off articles from [OpenAI](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html) and [Andrei Karpathy](https://karpathy.github.io/2016/05/31/rl/). Research from [Baeldung](https://www.baeldung.com/cs/rl-deterministic-vs-stochastic-policies#:~:text=The%20primary%20difference%20between%20a,over%20actions%20for%20each%20state.)

## Running

```shell
cd /src/
python moving_model.py
```