import matplotlib.pyplot as plt
import numpy as np
from SensorSimulation import PosSensor,PosSensor_1
from filterpy.kalman import KalmanFilter
from scipy.linalg import block_diag
from filterpy.common import Q_discrete_white_noise

"""  Testing the Sensor with default time step 1  """
# pos, vel = (4, 3), (2, 1)
# sensor = PosSensor(pos, vel, noise_std=1)
# ps = np.array([sensor.read() for _ in range(50)])
# plt.scatter(ps[:,0], ps[:,1], marker='o', facecolor='none', edgecolor='black', s=50)

# plt.title("Sensor Simulation Result")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid(True) 
# plt.legend()
# plt.show()



"""  Testing the Sensor1  """
# pos, vel = (4, 3), (2, 1)
# sensor = PosSensor_1(pos, vel, noise_std=1, time_step=0.5)
# ps = np.array([sensor.read() for _ in range(50)])
# plt.scatter(ps[:,0], ps[:,1], marker='o', facecolor='none', edgecolor='black', s=50)

# plt.title("Sensor 1  Simulation Result")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid(True) 
# plt.legend()
# plt.show()



"""Design state transition matrix"""
tracker = KalmanFilter(dim_x=4, dim_z=2)
dt = 1.   # time step 1 second
tracker.F = np.array([[1, dt, 0,  0],
                      [0,  1, 0,  0],
                      [0,  0, 1, dt],
                      [0,  0, 0,  1]])




"""Design the Process Noise Matrix"""
q = Q_discrete_white_noise(dim=2, dt=dt, var=0.001)
tracker.Q = block_diag(q, q)
print(tracker.Q)
