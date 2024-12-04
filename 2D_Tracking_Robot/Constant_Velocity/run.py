import matplotlib.pyplot as plt
import numpy as np
from filterpy.stats import plot_covariance_ellipse


from KalmanFilterDesign import tracker_2D_constant_velocity as tracker_2D_cv
from SensorSimulation import PosSensor,PosSensor_1

# Setting Q and R 
Q_std=0.1
R_std=0.5

# simulate robot movement
N = 30
sensor = PosSensor((0, 0), (2, .2), noise_std=R_std)
zs = np.array([sensor.read() for _ in range(N)])

# run filter
robot_tracker = tracker_2D_cv(Q_std,R_std).kf_2D_CV
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