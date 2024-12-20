from sensor_simulation import BallTrajectory2D
import matplotlib.pyplot as plt
import numpy as np
from filterpy.stats import plot_covariance_ellipse

def test_ball_vacuum(noise):
    y = 15
    x = 0
    ball = BallTrajectory2D(x0=x, y0=y, 
                            theta_deg=60., velocity=100., 
                            noise=noise)
    t = 0
    dt = 0.25
    while y >= 0:
        x, y = ball.step(dt)
        t += dt
        if y >= 0:
            plt.scatter(x, y, color='r', marker='.', s=75, alpha=0.5)
         
    
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7) 
    plt.axis('equal')
    plt.show()


    
#test_ball_vacuum([0, 0]) # plot ideal ball position
test_ball_vacuum([1, 1]) # plot with noise 