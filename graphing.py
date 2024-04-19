import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Constants
omega = 2 * np.pi * 500e12  # Angular frequency (rad/s)
c = 3e8  # Speed of light (m/s)
wave_number = omega / c

# Space and time domains
x = np.linspace(0, 1e-6, 400)  # 1 micron range
t = np.linspace(0, 1e-14, 100)  # Time range over one period of the wave

# Calculate the fields
E = np.cos(omega * t[:, None] - wave_number * x)  # Electric field (Ez)
B = np.cos(omega * t[:, None] - wave_number * x)  # Magnetic field (By)

# Create a 3D plot
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')

# Meshgrid for plotting
X, T = np.meshgrid(x, t)

# Plotting Electric Field
surf1 = ax.plot_surface(X, T, E, cmap='viridis', edgecolor='none', alpha=0.6, label='Electric Field (Ez)')
surf1._facecolors2d = surf1._facecolor3d
surf1._edgecolors2d = surf1._edgecolor3d

# Plotting Magnetic Field
surf2 = ax.plot_surface(X, T, B, cmap='plasma', edgecolor='none', alpha=0.6, label='Magnetic Field (By)')
surf2._facecolors2d = surf2._facecolor3d
surf2._edgecolors2d = surf2._edgecolor3d

# Labels and Titles
ax.set_xlabel('Position along x-axis (meters)')
ax.set_ylabel('Time (seconds)')
ax.set_zlabel('Field Amplitude')
ax.set_title('Visualization of Electromagnetic Wave Interaction with a Solar Panel')
ax.legend()

plt.show()
