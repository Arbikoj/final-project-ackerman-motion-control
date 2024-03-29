#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
import math
import matplotlib.pyplot as plt  
from matplotlib.animation import FuncAnimation
import numpy as np



def calculate_resultant_vector(angles, distances):
    if len(angles) != len(distances):
        raise ValueError("The lengths of angles and distances arrays must be the same.")

    angles_rad = [math.radians(angle) for angle in angles]

    x_components = [distance * math.cos(angle) for angle, distance in zip(angles_rad, distances)]
    y_components = [distance * math.sin(angle) for angle, distance in zip(angles_rad, distances)]

    resultant_x = sum(x_components)
    resultant_y = sum(y_components)

    resultant_magnitude = math.sqrt(resultant_x**2 + resultant_y**2)
    resultant_direction = math.degrees(math.atan2(resultant_y, resultant_x))

    return resultant_x, resultant_y, resultant_magnitude, resultant_direction

desired_angles = [0, 90, -90, -180, ]

def laser_callback(msg):
    ranges = msg.ranges
    angle_increment = msg.angle_increment
    angle_min = msg.angle_min

    desired_angles_radians = [math.radians(angle) for angle in desired_angles]
    
    distances = []
    angle_degrees_array = []

    # menambahkan Fgoal
    distances.append(2)
    angle_degrees_array.append(0)
        
    for angle in desired_angles_radians:
        index = int((angle - angle_min) / angle_increment)

        distance = ranges[index]

        angle_degrees = math.degrees(angle)

        print(f"Angle: {angle_degrees:.2f} degrees, Distance: {distance:.2f} meters")
        distances.append(distance)
        angle_degrees_array.append(angle_degrees)

        
    print("list sudut : ", distances)
        
    # print("Distances:", [f"{distance:.2f}" for distance in distances])
    # print("Distances :", distances)
    # print("Degrees :", angle_degrees_array)
    
    resultant_x, resultant_y, magnitude, direction = calculate_resultant_vector(angle_degrees_array, distances)

    print("Resultant X :", resultant_x)
    print("Resultant Y :", resultant_y)
    print("magnitude :", magnitude)
    print("direction :", direction)
    print("====================================================")
    print("")
    
        
def laser_subscriber():
    rospy.init_node('laser_subscriber', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, laser_callback)

    # fig = plt.figure()
    # ani = FuncAnimation(fig, update, interval=100)
    # plt.show()
    
    rospy.spin()
    



if __name__ == '__main__':
    try:
        laser_subscriber()
    except rospy.ROSInterruptException:
        pass