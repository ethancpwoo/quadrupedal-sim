import matplotlib.pyplot as plt
import numpy as np

class Grapher():

    def graph_params(self, rewards, dist, actor_loss, critic_loss, time, reward_vel, reward_time, reward_height, reward_rotation):
        
        fig, ax = plt.subplots(2, 2, constrained_layout = True)
        x = np.linspace(1, len(rewards), num=len(rewards))
        # print(rewards)
        ax[0,0].plot(x, rewards)
        ax[0,0].set_title('rewards')
        ax[0,1].plot(x, dist)
        ax[0,1].set_title('final dist')
        ax[1,0].plot(x, actor_loss)
        ax[1,0].set_title('actor_loss')
        ax[1,1].plot(x, critic_loss)
        ax[1,1].set_title('critic_loss')

        fig.savefig('./models/graph_hyper.png', dpi=1000)

        # fig, ax = plt.subplots(2, 2, constrained_layout = True)

        # ax[0,0].plot(x, time)
        # ax[0,0].set_title('time')
        # ax[0,1].plot(x, roll)
        # ax[0,1].set_title('roll')
        # ax[1,0].plot(x, pitch)
        # ax[1,0].set_title('pitch')
        # ax[1,1].plot(x, yaw)
        # ax[1,1].set_title('yaw')

        # fig.savefig('./models/graph_phys.png', dpi=1000)

        # fig, ax = plt.subplots(2, 2, constrained_layout = True)

        # ax[0,0].plot(x, reward_vel)
        # ax[0,0].set_title('reward_vel')
        # ax[0,1].plot(x, reward_time)
        # ax[0,1].set_title('reward_time')
        # ax[1,0].plot(x, reward_rotation)
        # ax[1,0].set_title('reward_rotation')
        # ax[1,1].plot(x, reward_height)
        # ax[1,1].set_title('reward_height')

        # fig.savefig('./models/graph_rewards.png', dpi=1000)


