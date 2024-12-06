import matplotlib.pyplot as plt
import numpy as np
from filterpy.stats import plot_covariance_ellipse

from kalman_filter_design import Tracker2DConstantAcceleration as Tracker2D
from sensor_simulation import PosSensor,PosSensor1
from ploting import *

# Setting Q and R 
Q_std=0.01
R_std=2
dt=1.0

# simulate robot movement
N = 30
sensor = PosSensor((0, 0), (0, 0), (0.1,0.2), noise_std=R_std)
zs = np.array([sensor.read() for _ in range(N)])

# run filter
robot_tracker = Tracker2D(Q_std,R_std,dt).kf_2D_CA
mu, cov, _, _ = robot_tracker.batch_filter(zs)

# output result
plot_measurement_estimate(mu,0,3,zs,0,1)
plot_2d_ellipse(mu,cov,0,3)
plot_2d_ellipse_measurement_estimate(mu,cov,0,3,zs,0,1)
plot_residue_variance(mu,cov,0,zs,0,dt)
plot_mean_variance(mu,cov,0,dt)
plot_mean_variance_measurement(mu,cov,0,zs,0,dt)
plt.pause(10**6)  # Pause indefinitely or for a very long time



