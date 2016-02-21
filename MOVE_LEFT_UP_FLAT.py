#!/usr/bin/env python

import rospy
import os
import baxter_interface
import baxter_external_devices
from baxter_interface import CHECK_VERSION

def main():
	rospy.init_node('hri_node', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	
	left = baxter_interface.Gripper('left', CHECK_VERSION)
	right = baxter_interface.Gripper('right', CHECK_VERSION)
	
	while not rospy.is_shutdown():
	
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/roberto/catkin_ws/src/articulated_object_manipulation/actions/right_reach_center.rec")
		
		right.close([])
		
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/roberto/catkin_ws/src/articulated_object_manipulation/actions/left_reach_left_up.rec")
		
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/roberto/catkin_ws/src/articulated_object_manipulation/actions/left_pullrotate_left_up_flat.rec")
		
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/roberto/catkin_ws/src/articulated_object_manipulation/actions/left_leave_left_flat.rec")
		
		right.open([])
		
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/roberto/catkin_ws/src/articulated_object_manipulation/actions/right_leave_center.rec")
		
		return;
		rospy.spin()


if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
