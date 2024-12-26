from sensor_simulation import BaseballPath,BallTrajectory2D
import matplotlib.pyplot as plt
import numpy as np
from filterpy.stats import plot_covariance_ellipse
from kalman_filter_design import  Tracker2DUnderGravity as Tracker2D

# def track_ball_vacuum(dt):
#     x, y = 0., 1.
#     theta = 35.  # launch angle
#     v0 = 80.
#     g = np.array([[-9.8]])  # gravitational constant
#     ball = BallTrajectory2D(x0=x, y0=y, theta_deg=theta, velocity=v0, 
#                             noise=[.2, .2])
#     kf = Tracker2D(x, y, theta, v0, dt).kf_2D_UG
    
#     print(kf.x)
#     t = 0
#     xs, ys = [], []
#     while kf.x[2] > 0:
#         t += dt
#         x, y = ball.step(dt)
#         z = np.array([[x, y]]).T

#         kf.update(z)
#         xs.append(kf.x[0])
#         ys.append(kf.x[2])    
#         kf.predict(u=g)     
#         p1 = plt.scatter(x, y, color='r', marker='.', s=75, alpha=0.5)
#     p2, = plt.plot(xs, ys, lw=2)
#     plt.legend([p2, p1], ['Kalman filter', 'Measurements'],
#                scatterpoints=1)
#     return kf
    
# track_ball_vacuum(dt=1./10)
# plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
# plt.show()




x, y = 0, 1.
theta = 35. # launch angle
v0 = 50.
dt = 1/10.   # time step
g = np.array([[-9.8]])

plt.figure()
ball = BaseballPath(x0=x, y0=y, launch_angle_deg=theta,
                    velocity_ms=v0, noise=[.3,.3])
f1 = Tracker2D(x, y, theta, v0, dt, Q_std=0.3,R_std=0.1).kf_2D_UG
f2 = Tracker2D(x, y, theta, v0, dt, Q_std=0.3,R_std=10).kf_2D_UG
t = 0
xs, ys = [], []
xs2, ys2 = [], []

while f1.x[2] > 0:
    t += dt
    x, y = ball.update(dt)
    z = np.array([[x, y]]).T

    f1.update(z)
    f2.update(z)
    xs.append(f1.x[0])
    ys.append(f1.x[2])
    xs2.append(f2.x[0])
    ys2.append(f2.x[2])    
    f1.predict(u=g) 
    f2.predict(u=g)
    
    p1 = plt.scatter(x, y, color='r', marker='.', s=75, alpha=0.5)

p2, = plt.plot(xs, ys, lw=2)
p3, = plt.plot(xs2, ys2, lw=4)
plt.legend([p1, p2, p3], 
           ['Measurements', 'Filter(R=0.1)', 'Filter(R=10)'],
           loc='best', scatterpoints=1);

plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.show()

