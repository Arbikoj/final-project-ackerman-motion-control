#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to compute the resultant vector
def compute_resultant(vectors):
    return np.sum(vectors, axis=0)

# Function to update the plot for each frame of the animation
def update(frame):
    # Generate random vectors
    vectors = np.random.rand(num_vectors, 2) * 10 - 5  # Random vectors between -5 and 5
    resultant_vector = compute_resultant(vectors)

    # Update plot
    ax.clear()
    ax.quiver(*vectors.T, angles='xy', scale_units='xy', scale=1, color='blue', label='Vectors')
    ax.quiver(0, 0, resultant_vector[0], resultant_vector[1], angles='xy', scale_units='xy', scale=1, color='red', label='Resultant Vector')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal', adjustable='box')
    ax.legend()

# Number of random vectors
num_vectors = 5

# Create a figure and axis
fig, ax = plt.subplots()

# Create animation
ani = FuncAnimation(fig, update, frames=range(10), interval=20)

plt.show()