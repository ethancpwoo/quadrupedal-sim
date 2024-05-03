# quadrupedal-sim

## Overview

Using PyBullet to simulate quadrupedal robotic movement. 

moving_model.py is for testing each joint in the URDF file.

Current implementation does not have mimiced joints nor defined constraints within PyBullet. Thigh and Foot are independent DOFs.

## RL Approach and Method

Reward function will be based on the position of the chassis. Unlike the Solo12 or other high level quadrupeds using joint-independent reward functions, this quadruped will use the chassis' RPY + velocity.

Model-Free learning, using Policy Gradient for direct optimazation of walking the quadruped. Stochastic Policy to capture uncertainty of realistic walking.

## Encountered Problem Log

1) Problem encountered was the fact that most PGs are essentially Markov Chains which will end up having only 1 probabilistic action. Vanilla Policy Gradients and the REINFORCE algorithm are simple on-policy algorithms. Probabilities for each action is generated from the agent and the action with the highest probability is selected. This is insufficient for the robot as position values are required + deterministic action.

Multiple approaches can be taken to get a 12-continous action space from the internet. DDPG and Hierachal Policy Gradients are popular approaches to solve this problem. (Starcraft 2){https://arxiv.org/abs/1708.04782} agent uses A3C, which can also handle large action spaces and has an incredibly complex agent structure. 

2) Curse of dimensionality for this problem as well. Is a 12-continuous action space sufficient? 

# Resources:

[reddit](https://www.reddit.com/r/MachineLearning/comments/9z8tok/d_reinforcement_learning_with_multiple/)

or 
[git](https://pemami4911.github.io/blog/2016/08/21/ddpg-rl.html#References)
[stack](https://stackoverflow.com/questions/43881897/what-is-the-policy-gradient-when-multiple-actions-are-possible)
[hk_ddpg](https://yanpanlau.github.io/2016/10/11/Torcs-Keras.html)
[ddg_blog](https://pemami4911.github.io/blog/2016/08/21/ddpg-rl.html#References)

Based off articles from [OpenAI](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html) and [Andrei Karpathy](https://karpathy.github.io/2016/05/31/rl/). Research from [Baeldung](https://www.baeldung.com/cs/rl-deterministic-vs-stochastic-policies#:~:text=The%20primary%20difference%20between%20a,over%20actions%20for%20each%20state.)

## Training Process

Agent will be provided chassis velocity, position and RPY. Agent will generate action consisting of position control values for each DOF every 60 timesteps or every .25 seconds. Simulation will reset every 10 seconds (each episode is 10 seconds) and gradient will be updated after 100 episodes.

# Reward Values

$`\ Yaw\:Reward = -0.01 * |Yaw| `$

$`\ Roll\:Reward = -0.01 * |Roll| `$

$`\ Pitch\:Reward = -0.01 * |Pitch| `$

$`\ Velocity\:Reward = 0.05 * V_x `$

$`\ X_{pos}\:Reward = 0.05 * (x - x_{last}) `$

$`\ Y_{pos}\:Reward = -0.01 * |y - y_{last}| `$

$`\ Z_{pos}\:Reward = -0.01 * |z - z_{last}| `$

## Running

```shell
cd /src/
python moving_model.py
```
