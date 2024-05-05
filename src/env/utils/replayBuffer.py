import random

from collections import deque


class ReplayBuffer():

    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.num_added = 0
        self.buffer = deque()
    
    def get_batch(self, batch_size):
        if self.num_added < batch_size:
            return random.sample(self.buffer, self.num_added)
        else:
            return random.sample(self.buffer, batch_size)
        
    def add(self, observation, action, reward, new_state, done):
        experience = (observation, action, reward, new_state, done)
        if self.num_added < self.buffer_size:
            self.buffer.append(experience)
            self.num_added += 1
        else:
            self.buffer.popleft()
            self.buffer.append(experience)
