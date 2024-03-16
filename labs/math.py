import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the differential equation
def dydx(x, y):
    return 9*y**2 - y**4

# Create a grid of x and y values for plotting the slope field
y, x = np.mgrid[-4:4:20j, -2:2:20j]

# Compute the slope (dy/dx) at each grid point
u = 1
v = dydx(x, y)

# Normalize the arrows
norm = np.sqrt(u**2 + v**2)
u /= norm
v /= norm

plt.quiver(x, y, u, v, norm, angles="xy")

# Plot trajectories with different initial conditions
for y0 in np.linspace(-3.5, 3.5, 7):
    sol = solve_ivp(dydx, [x.min(), x.max()], [y0], dense_output=True)
    y = sol.sol(np.linspace(-2, 2, 100))
    plt.plot(np.linspace(-2, 2, 100), y.T, color='black')

plt.xlabel('x')
plt.ylabel('y')
plt.xlim([-2, 2])
plt.ylim([-4, 4])
plt.title('Phase Portrait of dy/dx = 9y^2 - y^4')
plt.show()
