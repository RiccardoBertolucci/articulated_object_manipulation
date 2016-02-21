#!/usr/bin/env python

import rospy
import os
import subprocess
import sys

def main():
	rospy.init_node('hri_node', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	
	while not rospy.is_shutdown():

		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/roberto/catkin_ws/src/articulated_object_manipulation/actions/start_position.rec")

		os.system("python /home/roberto/catkin_ws/src/articulated_object_manipulation/scripts/MOVE_LEFT_FLAT_DOWN.py")

		os.system("python /home/roberto/catkin_ws/src/articulated_object_manipulation/scripts/MOVE_RIGHT_FLAT_DOWN.py")
			
		return;
		rospy.spin()


if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
