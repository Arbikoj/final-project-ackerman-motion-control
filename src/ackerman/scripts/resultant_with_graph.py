#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
def calculate_resultant_vector(angles, distances):
    # Ensure the lengths of angles and distances arrays are the same
    if len(angles) != len(distances):
        raise ValueError("The lengths of angles and distances arrays must be the same.")

    angles_rad = [math.radians(angle) for angle in angles]

    # Calculate horizontal and vertical components of each vector
    x_components = [distance * math.cos(angle) for angle, distance in zip(angles_rad, distances)]
    y_components = [distance * math.sin(angle) for angle, distance in zip(angles_rad, distances)]

    # Calculate the sum of horizontal and vertical components
    resultant_x = sum(x_components)
    resultant_y = sum(y_components)

    # Calculate the magnitude and direction of the resultant vector
    resultant_magnitude = math.sqrt(resultant_x**2 + resultant_y**2)
    resultant_direction = math.degrees(math.atan2(resultant_y, resultant_x))


    # Create a plot
    plt.figure()
    
    # Plot each vector
    for i in range(len(angles)):
        plt.quiver(0, 0, x_components[i], y_components[i], angles='xy', scale_units='xy', scale=1, color='blue', label=f'Vector {i + 1}')

    plt.quiver(0, 0, resultant_x, resultant_y, angles='xy', scale_units='xy', scale=1, color='red', label=f'Vector {i + 1}')
    # Set the aspect ratio of the plot to be equal
    plt.axis('equal')

    # Set labels for the axes
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.xticks([-12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12])

    # Set specific values for y-axis ticks
    plt.yticks([-12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12])
    # Set a title for the plot
    plt.title('Vectors in Matplotlib')

    # Add a legend
    plt.legend()

    # Display the plot
    plt.show()
    
    
    return resultant_x, resultant_y, resultant_magnitude, resultant_direction

# Example usage
angles_degrees = [45, 300.96, 154.43, 348.69]
distances = [4.24, 5.83, 6.59, 10.2]

resultant_x, resultant_y, magnitude, direction = calculate_resultant_vector(angles_degrees, distances)

print(f"Resultant Vector:")
print(f"Horizontal Component: {resultant_x:.2f}")
print(f"Vertical Component: {resultant_y:.2f}")
print(f"Magnitude: {magnitude:.2f}")
print(f"Direction: {direction:.2f} degrees")
print(f"Direction: {direction+360} dgre")
