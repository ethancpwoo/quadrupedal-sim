import numpy as np
import random

class OU():
    
    def OU(self, x, mu, theta, sigma):
        return theta * (mu - x) + (sigma * np.random.randn(1))
