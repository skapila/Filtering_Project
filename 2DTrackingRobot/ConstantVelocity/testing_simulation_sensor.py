from sensor_simulation import PosSensor,PosSensor1
import matplotlib.pyplot as plt
import numpy as np



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
pos, vel = (4, 3), (2, 1)
sensor = PosSensor1(pos, vel, noise_std=1, time_step=0.5)
ps = np.array([sensor.read() for _ in range(50)])
plt.scatter(ps[:,0], ps[:,1], marker='o', facecolor='none', edgecolor='black', s=50)

plt.title("Sensor 1  Simulation Result")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True) 
plt.legend()
plt.show()
