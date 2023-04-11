#! /usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray 

rospy.init_node('listener', anonymous=True)
pub = rospy.Publisher('dnndata', Float32MultiArray, queue_size=10)
rate = rospy.Rate(10)

data_list = [0,0,0,0,0,0,0]

def callback1(data):
	rospy.loginfo(rospy.get_caller_id() + " hum : %f", data.data)
	d1 = data.data / 6
	data_list[4]= d1

def callback2(data):
	rospy.loginfo(rospy.get_caller_id() + " temp : %f", data.data)
	data_list[3] = data.data
	
def callback3(data):
	rospy.loginfo(rospy.get_caller_id() + " vibrations : %f", data.data)
	data_list[6] = data.data
	
def callback4(data):
	rospy.loginfo(rospy.get_caller_id() + " alpha-decay : %f", data.data)
	data_list[0] = data.data
	
def callback5(data):
	rospy.loginfo(rospy.get_caller_id() + " beta-decay : %f", data.data)
	data_list[1] = data.data

def callback6(data):
	rospy.loginfo(rospy.get_caller_id() + " gamma-decay : %f", data.data)
	data_list[2] = data.data
	
def callback7(data):
	rospy.loginfo(rospy.get_caller_id() + " pressure : %f", data.data)
	data_list[5] = data.data
	msg = Float32MultiArray(data=data_list)
	pub.publish(msg)

def listener():
	rospy.Subscriber("humvalue", Float32,callback1)
	rospy.Subscriber("tempvalue", Float32,callback2)
	rospy.Subscriber("vibvalue",Float32,callback3)
	rospy.Subscriber("ARadivalue",Float32,callback4)
	rospy.Subscriber("BRadivalue",Float32,callback5)
	rospy.Subscriber("GRadivalue",Float32,callback6)
	rospy.Subscriber("pressure",Float32,callback7)
	
	
	#data_list = [0, 0, 0, 0, 0, 0, 0]
	rate.sleep()
	rospy.spin()
	print(data_list)
	
	
if __name__ == '__main__':
	listener()
	
