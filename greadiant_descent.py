import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

sp.init_printing()

# Define symbolic variables
x1, x2 = sp.symbols('x1 x2')

# Define the function
fg = 5*x1**2 + x2**2 + 4*x1*x2 - 14*x1 - 6*x2 + 20

# Create a mesh grid for plotting
x1_values = np.linspace(-10, 10, 400)
x2_values = np.linspace(-10, 10, 400)
X1, X2 = np.meshgrid(x1_values, x2_values)
Z = np.array([[fg.subs({x1: val1, x2: val2}) for val1 in x1_values] for val2 in x2_values])

# Plot the surface
fig = plt.figure()
# ax = fig.gca(projection='3d')
ax.plot_surface(X1, X2, Z, cmap='viridis')
plt.pause(5)

# Initialize variables
x1_val = -10
x2_val = -10

# Create lists to store the trajectory
x1_traj = [x1_val]
x2_traj = [x2_val]
fg_traj = [fg.subs({x1: x1_val, x2: x2_val})]

# Perform gradient descent
learning_rate = 0.001
for h in range(50000):
    x1_val -= learning_rate * sp.diff(fg, x1).subs({x1: x1_val, x2: x2_val})
    x2_val -= learning_rate * sp.diff(fg, x2).subs({x1: x1_val, x2: x2_val})
    fg_val = fg.subs({x1: x1_val, x2: x2_val})
    x1_traj.append(x1_val)
    x2_traj.append(x2_val)
    fg_traj.append(fg_val)

    if h % 500 == 0:
        print(f'Iteration {h}: x1 = {x1_val:.4f}, x2 = {x2_val:.4f}, f(x1, x2) = {fg_val:.4f}')

# Plot the trajectory
ax.plot(x1_traj, x2_traj, fg_traj, 'ko-', markersize=5)
plt.show()
