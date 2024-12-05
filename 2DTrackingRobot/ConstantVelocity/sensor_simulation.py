from numpy.random import randn

class PosSensor(object):
    def __init__(self, pos=(0, 0), vel=(0, 0), noise_std=1.):
        self.vel = vel
        self.noise_std = noise_std
        self.pos = [pos[0], pos[1]]
        
    def read(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        return [self.pos[0] + randn() * self.noise_std,
                self.pos[1] + randn() * self.noise_std]
    


class PosSensor1(object):
    def __init__(self, pos=(0, 0), vel=(0, 0), noise_std=1., time_step=1.):
        self.vel = vel
        self.noise_std = noise_std
        self.pos = [pos[0], pos[1]]
        self.time_step=time_step
        
    def read(self):
        self.pos[0] += (self.vel[0]*self.time_step)
        self.pos[1] += (self.vel[1]*self.time_step)
        
        return [self.pos[0] + randn() * self.noise_std,
                self.pos[1] + randn() * self.noise_std]    