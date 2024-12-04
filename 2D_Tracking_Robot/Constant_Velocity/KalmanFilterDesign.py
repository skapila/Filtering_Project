from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
import numpy as np
from scipy.linalg import block_diag


class tracker_2D_constant_velocity(): 
    def __init__(self,Q_std=0.0,R_std=0.0):
        self.Q_std = Q_std
        self.R_std = R_std
        self.kf_2D_CV= self.tracker_2D(Q_std,R_std) 
        
    def tracker_2D(self,Q_std,R_std):
        """Design state transition matrix"""
        tracker = KalmanFilter(dim_x=4, dim_z=2)
        dt = 1.   # time step 1 second
        tracker.F = np.array([[1, dt, 0,  0],
                            [0,  1, 0,  0],
                            [0,  0, 1, dt],
                            [0,  0, 0,  1]])

        """Design the Process Noise Matrix"""
        q = Q_discrete_white_noise(dim=2, dt=dt, var=Q_std**2)
        tracker.Q = block_diag(q, q)


        """Design the Measurement Function"""
        tracker.H = np.array([[1, 0, 0,        0],
                            [0,        0, 1, 0]])


        """Design the Measurement Noise Matrix"""
        tracker.R = np.eye(2) * R_std**2

        """Initial Conditions"""
        tracker.x = np.array([[0, 0, 0, 0]]).T
        tracker.P = np.eye(4) * 500.

        return tracker