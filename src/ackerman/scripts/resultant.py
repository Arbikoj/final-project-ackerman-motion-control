#!/usr/bin/env python3
import math
# menghitung resultant dari value sensor lidar

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
