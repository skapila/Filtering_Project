import matplotlib.pyplot as plt
import numpy as np
from filterpy.stats import plot_covariance_ellipse

from kalman_filter_design import Tracker2DConstantVelocity as Tracker2D
from sensor_simulation import PosSensor,PosSensor1
from ploting import *

# Setting Q and R 
Q_std=0.01
R_std=0.35
dt=1.0

# simulate robot movement
N = 30
sensor = PosSensor((0, 0), (2, .2), noise_std=R_std)
zs = np.array([sensor.read() for _ in range(N)])

# run filter
robot_tracker = Tracker2D(Q_std,R_std,dt).kf_2D_CV
mu, cov, _, _ = robot_tracker.batch_filter(zs)

# output result
plot_measurement_estimate(mu,zs)
plot_2d_ellipse(mu,cov,0,2)
plot_2d_ellipse_measurement_estimate(mu,cov,0,2,zs)
plot_residue_variance(mu,cov,0,zs,dt)
plt.pause(10**6)  # Pause indefinitely or for a very long time



