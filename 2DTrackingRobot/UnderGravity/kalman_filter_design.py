from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
import numpy as np
from scipy.linalg import block_diag
from math import sin, cos, radians

class Tracker2DUnderGravity(): 
    def __init__(self,x,y,omega,v0,dt,Q_std=0.0,R_std=0.5):
        self.x=x
        self.y=y
        self.omega=omega
        self.v0=v0
        self.dt=dt

        self.Q_std = Q_std
        self.R_std = R_std
        self.kf_2D_UG= self.tracker_2D(x,y,omega,v0,dt,Q_std,R_std) 
        
    def tracker_2D(self,x,y,omega,v0,dt,Q_std,R_std):
        """Design state transition matrix"""
        kf = KalmanFilter(dim_x=4, dim_z=2, dim_u=1)
        kf.F = np.array([[1., dt, 0., 0.],   # x   = x0 + dx*dt
                            [0., 1., 0., 0.],   # dx  = dx0
                            [0., 0., 1., dt],   # y   = y0 + dy*dt
                            [0., 0., 0., 1.]])  # dy  = dy0

        kf.H = np.array([[1., 0., 0., 0.],
                            [0., 0., 1., 0.]])

        kf.B = np.array([[0., 0., 0., dt]]).T
        kf.R *= (R_std**2)
        kf.Q *= (Q_std**2)

        omega = radians(omega)
        vx = cos(omega) * v0
        vy = sin(omega) * v0
        kf.x = np.array([[x, vx, y, vy]]).T
        return kf

  