import math

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
angles_degrees = [30, 45, 60, 90]
distances = [5, 8, 6, 10]

resultant_x, resultant_y, magnitude, direction = calculate_resultant_vector(angles_degrees, distances)

print(f"Resultant Vector:")
print(f"Horizontal Component: {resultant_x:.2f}")
print(f"Vertical Component: {resultant_y:.2f}")
print(f"Magnitude: {magnitude:.2f}")
print(f"Direction: {direction:.2f} degrees")