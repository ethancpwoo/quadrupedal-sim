# quadrupedal-sim

## Overview

Using PyBullet to simulate quadrupedal robotic movement. 

moving_model.py is for testing each joint in the URDF file.

The current implementation does not have mimicked joints nor defined constraints within PyBullet. Thigh and Foot are independent DOFs.

## RL Approach and Method

The reward function will be based on the position of the chassis. Unlike the Solo12 or other high-level quadrupeds using joint-independent reward functions (hierarchal policy gradient), this quadruped will use the chassis' RPY + velocity.

Model-Free learning, using Policy Gradient for direct optimization of walking the quadruped. DDPG (Deterministic Deep Policy Gradients) will be the approach for this problem. It is an actor-critic algorithm, the actor being a policy gradient and the critic being a DQN or Q-Network. The actor trains off the DQNs results and the rewards of its actions. The value function does not see the policy's actions which makes it off policy. This process is called Temporal Difference learning and is a form of bootstrapping. 

## Encountered Problem Log

1) The problem encountered was that most PGs are essentially Markov Chains which will have only 1 probabilistic action. Vanilla Policy Gradients and the REINFORCE algorithm are simple on-policy algorithms. Probabilities for each action are generated from the agent and the action with the highest probability is selected. The negative values are multiplied with standardized rewards and summed as the loss where SGD optimizes it. This is insufficient for the robot as position values are required + deterministic action.\
Multiple approaches can be taken to get a 12-continuous action space from the internet. DDPG and Hierarchal Policy Gradients are popular approaches to solve this problem. (Starcraft 2){https://arxiv.org/abs/1708.04782} agent uses A3C, which can also handle large action spaces and has an incredibly complex agent structure.\
It is possible to map the stochastic policy to the min and maxes of each joint and try to do one action at a time. However, if I were to do this, it would be a wiser use of time to implement DDPG as the robot would be deterministic and would be able to have multiple actions at a time. DDPG only supports continuous action spaces with a deterministic policy, perfect for this application.

2) Curse of dimensionality for this problem as well. From DQN to PGs this problem remains as deterministic or stochastic problems can have trouble mapping the network output to discrete action spaces. For the quadruped robot, the joint can move around 1.07 rad each which could be discretized to 0.2 rad since both DQNs and PGs can only produce 1 discrete action (to move 0.2 rad or not to move 0.2 rad). Would this 0.2 rad be too much or too little? If we were to do this for each joint it would increase exponentially, thus a continuous action space would be required. (actually PGs can bypass this problem through interpreting the output as $`\ log(theta) `$ to sample any number, instead of output of $`\ mu `$ see [this](https://datascience.stackexchange.com/questions/61707/policy-gradient-with-continuous-action-space)) 

## Training Process

Agent will be provided chassis velocity, position and RPY. Agent will generate action consisting of position control values for each DOF every 60 timesteps or every .25 seconds. Simulation will reset every 10 seconds (each episode is 10 seconds) and gradient will be updated after 100 episodes.

## Reward Values

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
## Resources:

[reddit](https://www.reddit.com/r/MachineLearning/comments/9z8tok/d_reinforcement_learning_with_multiple/) \ 
[git](https://pemami4911.github.io/blog/2016/08/21/ddpg-rl.html#References) \
[stack](https://stackoverflow.com/questions/43881897/what-is-the-policy-gradient-when-multiple-actions-are-possible) \
[torcs_ddpg](https://yanpanlau.github.io/2016/10/11/Torcs-Keras.html) \
[ddg_blog](https://pemami4911.github.io/blog/2016/08/21/ddpg-rl.html#References) \
[Baeldung](https://www.baeldung.com/cs/rl-deterministic-vs-stochastic-policies#:~:text=The%20primary%20difference%20between%20a,over%20actions%20for%20each%20state.)

Inspiration articles from [OpenAI](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html) and [Andrei Karpathy](https://karpathy.github.io/2016/05/31/rl/).
