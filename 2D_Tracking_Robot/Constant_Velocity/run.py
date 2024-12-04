import matplotlib.pyplot as plt
import numpy as np
from SensorSimulation import PosSensor,PosSensor_1
from filterpy.kalman import KalmanFilter
from scipy.linalg import block_diag
from filterpy.common import Q_discrete_white_noise
from filterpy.stats import plot_covariance_ellipse


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

def tracker_2D(Q_std,R_std):

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
    print(tracker.Q)


    """Design the Measurement Function"""
    tracker.H = np.array([[1, 0, 0,        0],
                        [0,        0, 1, 0]])


    """Design the Measurement Noise Matrix"""
    tracker.R = np.eye(2) * R_std**2

    """Initial Conditions"""
    tracker.x = np.array([[0, 0, 0, 0]]).T
    tracker.P = np.eye(4) * 500.

    return tracker

# Setting Q and R 
Q_std=0.1
R_std=0.5

# simulate robot movement
N = 30
sensor = PosSensor((0, 0), (2, .2), noise_std=R_std)
zs = np.array([sensor.read() for _ in range(N)])

# run filter
robot_tracker = tracker_2D(Q_std,R_std)
mu, cov, _, _ = robot_tracker.batch_filter(zs)

for x, P in zip(mu, cov):
    # covariance of x and y
    cov = np.array([[P[0, 0], P[2, 0]], 
                    [P[0, 2], P[2, 2]]])
    mean = (x[0, 0], x[2, 0])
    plot_covariance_ellipse(mean, cov=cov, fc='g', std=3, alpha=0.5)

# Plot the trend line
plt.plot(mu[:, 0], mu[:, 2], label="Filter", color='blue', linewidth=2)

# Plot the measurements as concentric circles
plt.scatter(zs[:, 0], zs[:, 1], label="Measurements", marker='o', facecolor='none', edgecolor='black', s=3, linewidths=1.5)

# Add grid, labels, and legend
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.title("Filtered Data with Measurements")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()    
plt.show()