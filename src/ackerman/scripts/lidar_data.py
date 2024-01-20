#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
import math

def laser_callback(msg):
    # Extracting information from LaserScan message
    ranges = msg.ranges
    angle_increment = msg.angle_increment
    angle_min = msg.angle_min

    # Iterate through the ranges and print distance and angle information
    for i, distance in enumerate(ranges):
        # Calculate the current angle
        angle = angle_min + i * angle_increment

        # Convert angle from radians to degrees
        angle_degrees = math.degrees(angle)

        print(f"Angle: {angle_degrees:.2f} degrees, Distance: {distance:.2f} meters")

def laser_subscriber():
    rospy.init_node('laser_subscriber', anonymous=True)
    
    # Subscribe to the LaserScan topic
    rospy.Subscriber('/scan', LaserScan, laser_callback)

    # Keep the script running
    rospy.spin()

if __name__ == '__main__':
    try:
        laser_subscriber()
    except rospy.ROSInterruptException:
        pass