#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
import math

# Define the desired angles in degrees
desired_angles = [0, 90, 180, -80]

def laser_callback(msg):
    ranges = msg.ranges
    angle_increment = msg.angle_increment
    angle_min = msg.angle_min

# Convert desired angles from degrees to radians
    desired_angles_radians = [math.radians(angle) for angle in desired_angles]

    # Extract distances at desired angles
    for angle in desired_angles_radians:
        # Calculate the index corresponding to the desired angle
        index = int((angle - angle_min) / angle_increment)

        # Get the distance at the desired angle
        distance = ranges[index]

        # Convert angle from radians to degrees for printing
        angle_degrees = math.degrees(angle)

        print(f"Angle: {angle_degrees:.2f} degrees, Distance: {distance:.2f} meters")


def laser_subscriber():
    rospy.init_node('laser_subscriber', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, laser_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        laser_subscriber()
    except rospy.ROSInterruptException:
        pass