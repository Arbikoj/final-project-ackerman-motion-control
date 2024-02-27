#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
import math
import matplotlib.pyplot as plt  
from matplotlib.animation import FuncAnimation

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


    # Plot each vector
    # for i in range(len(angles)):
    #     plt.quiver(0, 0, x_components[i], y_components[i], angles='xy', scale_units='xy', scale=1, color='blue', label=f'Vector {i + 1}')

    # plt.quiver(0, 0, resultant_x, resultant_y, angles='xy', scale_units='xy', scale=1, color='red', label=f'Vector {i + 1}')
    

    # Set labels for the axes
    # plt.xlabel('X-axis')
    # plt.ylabel('Y-axis')

    # plt.xticks([ -4, -2, 0, 2, 4])

    # Set specific values for y-axis ticks
    # plt.yticks([-4, -2, 0, 2, 4])
    # Set a title for the plot
    # plt.title('Lidar')

    # Add a legend
    # plt.legend()

    # Display the plot
    # plt.show()
    
    
    return resultant_x, resultant_y, resultant_magnitude, resultant_direction

# Function to update the plot in real-time
def update_plot(angles, distances):
    angles_rad = [math.radians(angle) for angle in angles]
    # Calculate horizontal and vertical components of each vector
    x_components = [distance * math.cos(angle) for angle, distance in zip(angles_rad, distances)]
    y_components = [distance * math.sin(angle) for angle, distance in zip(angles_rad, distances)]
    
    resultant_x = sum(x_components)
    resultant_y = sum(y_components)
    
    # Calculate the magnitude and direction of the resultant vector
    resultant_magnitude = math.sqrt(resultant_x**2 + resultant_y**2)
    resultant_direction = math.degrees(math.atan2(resultant_y, resultant_x))
    
    # resultant_x, resultant_y, resultant_magnitude, resultant_direction = generate_random_data()
    for i in range(len(angles)):
        plt.quiver(0, 0, x_components[i], y_components[i], angles='xy', scale_units='xy', scale=1, color='blue', label=f'Vector {i + 1}')

    plt.quiver(0, 0, resultant_x, resultant_y, angles='xy', scale_units='xy', scale=1, color='red', label=f'Vector {i + 1}')
    return resultant_x, resultant_y, resultant_magnitude, resultant_direction
    
# Define the desired angles in degrees
desired_angles = [0, 90, -90, 180]

def laser_callback(msg):
    ranges = msg.ranges
    angle_increment = msg.angle_increment
    angle_min = msg.angle_min

    desired_angles_radians = [math.radians(angle) for angle in desired_angles]
    
    distances = []
    angle_degrees_array = []
    
    # Extract distances at desired angles
    for angle in desired_angles_radians:
        # Calculate the index corresponding to the desired angle
        index = int((angle - angle_min) / angle_increment)

        # Get the distance at the desired angle
        distance = ranges[index]

        # Convert angle from radians to degrees for printing
        angle_degrees = math.degrees(angle)

        print(f"Angle: {angle_degrees:.2f} degrees, Distance: {distance:.2f} meters")
        distances.append(distance)
        angle_degrees_array.append(angle_degrees)
        
    # print("Distances:", [f"{distance:.2f}" for distance in distances])
    print("Distances :", distances)
    print("Degrees :", angle_degrees_array)
    resultant_x, resultant_y, magnitude, direction = calculate_resultant_vector(angle_degrees_array, distances)
    
    print("Resultant X :", resultant_x)
    print("Resultant Y :", resultant_y)
    print("magnitude :", magnitude)
    print("direction :", direction)
    
    
def laser_subscriber():
    rospy.init_node('laser_subscriber', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, laser_callback)
    fig, ax = plt.subplots()

    # Create an animation
    ani = FuncAnimation(fig, calculate_resultant_vector, frames=200, interval=1000, repeat=True)
    plt.show()
    rospy.spin()

if __name__ == '__main__':
    try:
        laser_subscriber()
    except rospy.ROSInterruptException:
        pass