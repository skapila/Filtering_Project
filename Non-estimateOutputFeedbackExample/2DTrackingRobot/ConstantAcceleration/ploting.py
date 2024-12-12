import matplotlib.pyplot as plt
import numpy as np
from filterpy.stats import plot_covariance_ellipse

def plot_measurement_estimate(x_est,i,j,Z_out,u,w):
    plt.figure(1)    
    # Plot the trend line
    plt.plot(x_est[:, i], x_est[:, j], label="Filter", color='blue', linewidth=2)

    # Plot the measurements as concentric circles
    plt.scatter(Z_out[:, u], Z_out[:, w], label="Measurements", marker='o', facecolor='none', edgecolor='black', s=3, linewidths=1.5)

    # Add grid, labels, and legend
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.title("Filtered Data with Measurements")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()    
    plt.show(block=False)

def plot_2d_ellipse(x_est,P_est,i,j):
    plt.figure(2)
    for x, P in zip(x_est, P_est):
        # covariance of x and y
        covariance = np.array([[P[i, i], P[j, i]], 
                        [P[i, j], P[j, j]]])
        mean = (x[i, 0], x[j, 0])
        plot_covariance_ellipse(mean, cov=covariance, fc='g', std=3, alpha=0.5)
    
    # Add grid, labels, and legend
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.title("Ellipse-Error of two state variable ")
    plt.xlabel("X"+str(i))
    plt.ylabel("X"+str(j))
    plt.legend()    
    plt.show(block=False)

def plot_2d_ellipse_measurement_estimate(x_est,P_est,i,j,z,u,w):
    plt.figure(3)
    for x, P in zip(x_est, P_est):
        # covariance of x and y
        covariance = np.array([[P[i, i], P[j, i]], 
                        [P[i, j], P[j, j]]])
        mean = (x[i, 0], x[j, 0])
        plot_covariance_ellipse(mean, cov=covariance, fc='g', std=3, alpha=0.5)
    
    # Plot the trend line
    plt.plot(x_est[:, i], x_est[:, j], label="Filter", color='blue', linewidth=2)

    # Plot the measurements as concentric circles
    plt.scatter(z[:, u], z[:, w], label="Measurements", marker='o', facecolor='none', edgecolor='black', s=3, linewidths=1.5)


    # Add grid, labels, and legend
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.title("Filtered Data with Measurements and ellipse error")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()    
    plt.show(block=False)



def plot_residue_variance(x_est,P_est,index,z,index2,dt=1):
    plt.figure(4)
    upper_bound=[]
    lower_bound=[]
    for x, P in zip(x_est, P_est):
        upper_bound.append(P[index,index]**(1/2))   # Upper bound for the yellow shaded region
        lower_bound.append(-P[index,index]**(1/2))  # Lower bound for the yellow shaded region
    res = np.array(z[:, index2]) - np.array(x_est[:, index][:, index])
    time = np.arange(0,len(res),dt)

    # Plot the main line
    plt.plot(time,res,label="Residue", color='blue', linewidth=1.5)

    # Fill the shaded region
    plt.fill_between(time, lower_bound, upper_bound, color='yellow', alpha=0.4, label="Confidence Interval")

    # Plot the dashed boundary lines
    plt.plot(time, upper_bound , 'k--', linewidth=1)  # Upper dashed line
    plt.plot(time, lower_bound , 'k--', linewidth=1)  # Lower dashed line

    # Add labels, grid, and title
    plt.title("Residuals of X_"+str(index)+" state variable")
    plt.xlabel("Time (sec)")
    plt.ylabel("Meters")
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

    # Display legend
    plt.legend()

    # Show the plot
    plt.show(block=False)

def plot_mean_variance(x_est,P_est,index,dt):
    plt.figure(5)
    upper_bound=[]
    lower_bound=[]
    for x, P in zip(x_est, P_est):
        upper_bound.append(P[index,index]**(1/2))   # Upper bound for the yellow shaded region
        lower_bound.append(-P[index,index]**(1/2))  # Lower bound for the yellow shaded region
    x = x_est[:, index][:, index]
    time = np.arange(0,len(x),dt)

    # Plot the main line
    plt.plot(time,x,label="Estimate", color='blue', linewidth=1.5)

    # Fill the shaded region
    plt.fill_between(time, lower_bound, upper_bound, color='yellow', alpha=0.4, label="Confidence Interval")

    # Plot the dashed boundary lines
    plt.plot(time, upper_bound , 'k--', linewidth=1)  # Upper dashed line
    plt.plot(time, lower_bound , 'k--', linewidth=1)  # Lower dashed line

    # Add labels, grid, and title
    plt.title("Estimate with variance of X_"+str(index)+" state variable")
    plt.xlabel("Time (sec)")
    plt.ylabel("Meters")
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

    # Display legend
    plt.legend()

    # Show the plot
    plt.show(block=False)


def plot_mean_variance_measurement(x_est,P_est,index,Z_out,index2,dt):
    plt.figure(6)
    upper_bound=[]
    lower_bound=[]
    for x, P in zip(x_est, P_est):
        upper_bound.append(P[index,index]**(1/2))   # Upper bound for the yellow shaded region
        lower_bound.append(-P[index,index]**(1/2))  # Lower bound for the yellow shaded region
    x = x_est[:, index][:, index]
    z = Z_out[:, index2]
    time = np.arange(0,len(x),dt)

    # Plot the main line
    plt.plot(time,x,label="Estimate", color='blue', linewidth=1.5)

    # Plot the measurment line
    plt.scatter(time,z, label="Measurements", marker='o', facecolor='none', edgecolor='black', s=3, linewidths=1.5)

    # Fill the shaded region
    plt.fill_between(time, lower_bound, upper_bound, color='yellow', alpha=0.4, label="Confidence Interval")

    # Plot the dashed boundary lines
    plt.plot(time, upper_bound , 'k--', linewidth=1)  # Upper dashed line
    plt.plot(time, lower_bound , 'k--', linewidth=1)  # Lower dashed line

    # Add labels, grid, and title
    plt.title("Estimate with Variance and Measurement of X_"+str(index)+" state variable")
    plt.xlabel("Time (sec)")
    plt.ylabel("Meters")
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

    # Display legend
    plt.legend()

    # Show the plot
    plt.show(block=False)
        