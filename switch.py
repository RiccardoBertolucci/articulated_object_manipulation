#!/usr/bin/env python

#=====================================================================================================
# Articulated Object Manipulation and Tracking
#
# Authors: Riccardo Bertolucci & Roberto Menicatti
# Emails:  richi.bertolucci@gmail.com - roberto.menicatti@hotmail.it
#
# EMARO 2nd year 2015/2016 - Software Architecture Project
#=====================================================================================================

import rospy
import os
import os.path
import baxter_interface
import baxter_external_devices
from baxter_interface import CHECK_VERSION

null,a,b,c,d,e,f,g,h,i = 'null', 'a', 'b', 'c','d','e','f','g','h','i'

current_configuration = a
out_file = null

def writeCurrentConfig(curr_config):
	print("=================================================================================")
	print("Reached configuration "+ curr_config + ", insert next goal configuration or")
	print("press ? to see the reachable configurations, Esc to quit.")	
	print("=================================================================================")


def newConfig( startConf1,startConf2,startConf3,endConf1,endConf2,endConf3):
	global current_configuration
	if current_configuration == startConf1:
		current_configuration = endConf1
		out_file.write("Moved from " + startConf1 +" to " + endConf1 + "\n \n")
		out_file.write("\n ----------------------------------------------- \n")
		writeCurrentConfig(endConf1)
	elif current_configuration == startConf2:
		current_configuration = endConf2
		out_file.write("Moved from " + startConf2 +" to " + endConf2 + "\n \n")
		out_file.write("\n ----------------------------------------------- \n")
		writeCurrentConfig(endConf2)
	elif current_configuration == startConf3:
		current_configuration = endConf3
		out_file.write("Moved from " + startConf3 +" to " + endConf3 + "\n \n")
		out_file.write("\n ----------------------------------------------- \n")
		writeCurrentConfig(endConf3)


def chose_configuration():
	# initialize interfaces
	print("Getting robot state... ")
	rs = baxter_interface.RobotEnable(CHECK_VERSION)
	init_state = rs.state().enabled
	left = baxter_interface.Gripper('left', CHECK_VERSION)
	right = baxter_interface.Gripper('right', CHECK_VERSION)

	def clean_shutdown():
		global out_file
		if not init_state:
			print("Disabling robot...")
			rs.disable()
			out_file.close()
			print("Exiting manipulations script.")
		rospy.on_shutdown(clean_shutdown)

	def move_left_flat_up():
		global out_file
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_reach_center\n")

		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_reach_center.rec")
		right.close([])

		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_reach_left_flat\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_reach_left_flat.rec")

		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_pushrotate_left_flat_up\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_pushrotate_left_flat_up.rec")

		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_leave_left_up\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_leave_left_up.rec")
		right.open([])

		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_leave_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_leave_center.rec")
		newConfig( a,b,d,f,e,h )
    
	def move_left_up_flat():
		global out_file
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_reach_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_reach_center.rec")
		right.close([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_reach_left_up\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_reach_left_up.rec")
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_pullrotate_left_up_flat\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_pullrotate_left_up_flat.rec")
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_leave_left_flat\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_leave_left_flat.rec")
		right.open([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_leave_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_leave_center.rec")
		newConfig( b,f,h,a,d,e )
        
	def move_left_flat_down():
		global out_file
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_reach_center\n")	
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_reach_center.rec")
		right.close([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_reach_left_flat\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_reach_left_flat.rec")
		left.close([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_rotate_left_flat_down\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_rotate_left_flat_down.rec")
		left.open([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_leave_left_down\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_leave_left_down.rec")
		right.open([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_leave_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_leave_center.rec")
		
		newConfig( a,d,e,c,i,g )
         
	def move_left_down_flat():
		global out_file
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_reach_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_reach_center.rec")
		right.close([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_reach_left_down\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_reach_left_down.rec")
		left.close([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_rotate_left_down_flat\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_rotate_left_down_flat.rec")
		left.open([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_leave_left_flat\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_leave_left_flat.rec")
		right.open([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_leave_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_leave_center.rec")
	 
	 	newConfig( c,i,g,a,d,e )
		
	def move_right_flat_up():
		global out_file
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_reach_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_reach_center.rec")
		left.close([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_reach_right_flat\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_reach_right_flat.rec")

		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_pushrotate_right_flat_up\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_pushrotate_right_flat_up.rec")
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_leave_right_up\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_leave_right_up.rec")
		left.open([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_leave_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_leave_center.rec")
		
		newConfig( a,b,c,d,f,i )
		
	def move_right_up_flat():
		global out_file
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_reach_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_reach_center.rec")
		left.close([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_reach_right_up\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_reach_right_up.rec")
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_pullrotate_right_up_flat\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_pullrotate_right_up_flat.rec")
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_leave_right_flat\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_leave_right_flat.rec")
		left.open([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_leave_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_leave_center.rec")
		
		newConfig( d,f,i,a,b,c )
		
	def move_right_flat_down():
		global out_file
		
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_reach_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_reach_center.rec")
		left.close([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_reach_right_flat\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_reach_right_flat.rec")
		right.close([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_rotate_right_flat_down\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_rotate_right_flat_down.rec")
		right.open([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_leave_right_down\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_leave_right_down.rec")
		left.open([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_leave_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_leave_center.rec")
	
		newConfig( a,b,c,e,h,g )
		
	def move_right_down_flat():
		global out_file
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_reach_center\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_reach_center.rec")
		left.close([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_reach_right_down\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_reach_right_down.rec")
		right.close([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_rotate_right_down_flat\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_rotate_right_down_flat.rec")
		right.open([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting right_leave_right_flat\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/right_leave_right_flat.rec")
		left.open([])
	
		out_file.write("Time: "+ str(rospy.Time.now()) + ": starting left_leave_cente\n")
		os.system("rosrun baxter_examples joint_trajectory_file_playback_modified.py -f /home/berto/ros_ws/src/articulated_object_manipulation/actions/left_leave_center.rec")
	
		newConfig( e,h,g,a,b,c )  

	configurations_from_a = {
	#   key: (function, args, description)
		'b': (move_left_flat_up,    [], "b"),
		'c': (move_left_flat_down,  [], "c"),
		'd': (move_right_flat_up,   [], "d"),
		'e': (move_right_flat_down, [], "e"),
	}
	configurations_from_b = {
	#   key: (function, args, description)
		'a': (move_left_up_flat,    [], "a"),
		'f': (move_right_flat_up,   [], "f"),
		'h': (move_right_flat_down, [], "h"),
	}
	configurations_from_c = {
	#   key: (function, args, description)
		'a': (move_left_down_flat,  [], "a"),
		'g': (move_right_flat_down, [], "g"),
		'i': (move_right_flat_up,   [], "i"),
	}
	configurations_from_d = {
	#   key: (function, args, description)
		'a': (move_right_up_flat,  [], "a"),
		'f': (move_left_flat_up,   [], "f"),
		'i': (move_left_flat_down, [], "i"),
	}
	configurations_from_e = {
	#   key: (function, args, description)
		'a': (move_right_down_flat, [], "a"),
		'g': (move_left_flat_down,  [], "g"),
		'h': (move_left_flat_up,    [], "h"),
	}
	configurations_from_f = {
	#   key: (function, args, description)
		'b': (move_right_up_flat, [], "b"),
		'd': (move_left_up_flat,  [], "d"),
	}	
	configurations_from_g = {
	#   key: (function, args, description)
		'c': (move_right_down_flat, [], "c"),
		'e': (move_left_down_flat,  [], "e"),
	}	
	configurations_from_h = {
	#   key: (function, args, description)
		'b': (move_right_down_flat, [], "b"),
		'e': (move_left_up_flat,    [], "e"),
	}	
	configurations_from_i = {
	#   key: (function, args, description)
		'c': (move_right_up_flat,  [], "c"),
		'd': (move_left_down_flat, [], "d"),
	}	
    
	done = False
	print("Enabling robot... ")
	rs.enable()
	print("=================================================================================")
	print("Current configuration is 'a', insert the goal configuration or")
	print("press ? to see the reachable configurations, Esc to quit.")
	print("=================================================================================")
	while not done and not rospy.is_shutdown():
		first_input = baxter_external_devices.getch()
		if first_input:
			if current_configuration == a:
			    if first_input in ['\x1b', '\x03']:
			        done = True
			    elif first_input in configurations_from_a:
			        cmd = configurations_from_a[first_input]
			        print("Move to configuration: %s" % (cmd[2],))			        
			        cmd[0](*cmd[1])
			    else:
			        print("key bindings: ")
			        print("  Esc: Quit")
			        print("  ?: Help")
			        for key, val in sorted(configurations_from_a.items(), key=lambda x: x[1][2]):
			            print("  %s: %s" % (key, val[2]))
			elif current_configuration == b:
			    if first_input in ['\x1b', '\x03']:
			        done = True
			    elif first_input in configurations_from_b:
			        cmd = configurations_from_b[first_input]
			        print("Move to configuration: %s" % (cmd[2],))			        
			        cmd[0](*cmd[1])
			    else:
			        print("key bindings: ")
			        print("  Esc: Quit")
			        print("  ?: Help")
			        for key, val in sorted(configurations_from_b.items(), key=lambda x: x[1][2]):
			            print("  %s: %s" % (key, val[2]))
			elif current_configuration == c:
			    if first_input in ['\x1b', '\x03']:
			        done = True
			    elif first_input in configurations_from_c:
			        cmd = configurations_from_c[first_input]
			        print("Move to configuration: %s" % (cmd[2],))			        
			        cmd[0](*cmd[1])
			    else:
			        print("key bindings: ")
			        print("  Esc: Quit")
			        print("  ?: Help")
			        for key, val in sorted(configurations_from_c.items(), key=lambda x: x[1][2]):
			            print("  %s: %s" % (key, val[2]))
			elif current_configuration == d:
			    if first_input in ['\x1b', '\x03']:
			        done = True
			    elif first_input in configurations_from_d:
			        cmd = configurations_from_d[first_input]
			        print("Move to configuration: %s" % (cmd[2],))			        
			        cmd[0](*cmd[1])
			    else:
			        print("key bindings: ")
			        print("  Esc: Quit")
			        print("  ?: Help")
			        for key, val in sorted(configurations_from_d.items(), key=lambda x: x[1][2]):
			            print("  %s: %s" % (key, val[2]))
			elif current_configuration == e:
			    if first_input in ['\x1b', '\x03']:
			        done = True
			    elif first_input in configurations_from_e:
			        cmd = configurations_from_e[first_input]
			        print("Move to configuration: %s" % (cmd[2],))			        
			        cmd[0](*cmd[1])
			    else:
			        print("key bindings: ")
			        print("  Esc: Quit")
			        print("  ?: Help")
			        for key, val in sorted(configurations_from_e.items(), key=lambda x: x[1][2]):
			            print("  %s: %s" % (key, val[2]))	
			elif current_configuration == f:
			    if first_input in ['\x1b', '\x03']:
			        done = True
			    elif first_input in configurations_from_f:
			        cmd = configurations_from_f[first_input]
			        print("Move to configuration: %s" % (cmd[2],))			       
			        cmd[0](*cmd[1])
			    else:
			        print("key bindings: ")
			        print("  Esc: Quit")
			        print("  ?: Help")
			        for key, val in sorted(configurations_from_f.items(), key=lambda x: x[1][2]):
			            print("  %s: %s" % (key, val[2]))
			elif current_configuration == g:
			    if first_input in ['\x1b', '\x03']:
			        done = True
			    elif first_input in configurations_from_g:
			        cmd = configurations_from_g[first_input]
			        print("Move to configuration: %s" % (cmd[2],))			        
			        cmd[0](*cmd[1])
			    else:
			        print("key bindings: ")
			        print("  Esc: Quit")
			        print("  ?: Help")
			        for key, val in sorted(configurations_from_g.items(), key=lambda x: x[1][2]):
			            print("  %s: %s" % (key, val[2]))	
			elif current_configuration == h:
			    if first_input in ['\x1b', '\x03']:
			        done = True
			    elif first_input in configurations_from_h:
			        cmd = configurations_from_h[first_input]
			        print("Move to configuration: %s" % (cmd[2],))			        
			        cmd[0](*cmd[1])
			    else:
			        print("key bindings: ")
			        print("  Esc: Quit")
			        print("  ?: Help")
			        for key, val in sorted(configurations_from_h.items(), key=lambda x: x[1][2]):
			            print("  %s: %s" % (key, val[2]))		
			elif current_configuration == i:
			    if first_input in ['\x1b', '\x03']:
			        done = True
			    elif first_input in configurations_from_i:
			        cmd = configurations_from_i[first_input]
			        print("Move to configuration: %s" % (cmd[2],))			        
			        cmd[0](*cmd[1])
			    else:
			        print("key bindings: ")
			        print("  Esc: Quit")
			        print("  ?: Help")
			        for key, val in sorted(configurations_from_i.items(), key=lambda x: x[1][2]):
			            print("  %s: %s" % (key, val[2]))		                                	                		                	                		       
	# force shutdown call if caught by key handler
	rospy.signal_shutdown("Manipulations finished.")


def main():
	print("Initializing node... ")
	rospy.init_node("switch")

	save_path = '/home/berto/ros_ws/src/articulated_object_manipulation/action_log_files'

	fileName = raw_input('Insert the file name: ')

	completeName = os.path.join(save_path, "action_log_" + str(fileName) +".txt")

	global out_file
	out_file = open(completeName,"w")

	out_file.write("=====================================================================================================\n\n")
	out_file.write("Articulated Object Manipulation and Tracking - action_log_" + str(fileName) + "\n")
	out_file.write("Authors: Riccardo Bertolucci & Roberto Menicatti\n")
	out_file.write("Emails:  richi.bertolucci@gmail.com - roberto.menicatti@hotmail.it\n\n")
	out_file.write("EMARO 2nd year 2015/2016 - Software Architecture Project\n\n")
	out_file.write("=====================================================================================================\n\n")

	chose_configuration()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass

