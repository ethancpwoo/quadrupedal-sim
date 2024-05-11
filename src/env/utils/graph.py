import matplotlib.pyplot as plt
import numpy as np

class Grapher():

    def graph_params(self, rewards, epsilons, actor_loss, critic_loss):
        fig = plt.figure()
        ax = fig.subplots(2, 2)
        x = np.linspace(1, len(rewards), num=len(rewards))
        # print(rewards)
        ax[0,0].plot(x, rewards)
        ax[0,0].set_title('rewards')
        ax[0,1].plot(x, epsilons)
        ax[0,1].set_title('final dist')
        ax[1,0].plot(x, actor_loss)
        ax[1,0].set_title('actor_loss')
        ax[1,1].plot(x, critic_loss)
        ax[1,1].set_title('critic_loss')
        fig.savefig('./models/graph.png')


