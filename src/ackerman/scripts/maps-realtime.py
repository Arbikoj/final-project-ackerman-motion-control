#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
import matplotlib.pyplot as plt

# Initialize empty arrays to hold laser scan data
ranges = []
angles = []

def laser_callback(msg):
    global ranges, angles
    ranges = msg.ranges
    angles = [msg.angle_min + i * msg.angle_increment for i in range(len(ranges))]

def plot_map():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    ax.set_ylim(0, 10)  # Set the range according to your laser's capabilities

    while not rospy.is_shutdown():
        ax.clear()
        ax.plot(angles, ranges, 'r.')  # Plot laser scan data
        plt.pause(0.01)

if __name__ == "__main__":
    rospy.init_node('map_plotter', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, laser_callback)
    plot_map()
