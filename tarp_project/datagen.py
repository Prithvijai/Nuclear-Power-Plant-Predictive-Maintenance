#! /usr/bin/env python3

import rospy
import random
from std_msgs.msg import Float32

alpharad =0
betarad = 0
gamarad = 0
pre = 0

rospy.init_node('datagen', anonymous=True)
pub1 =rospy.Publisher("ARadivalue",Float32,queue_size=10)
pub2 =rospy.Publisher("BRadivalue",Float32,queue_size=10)
pub3 =rospy.Publisher("GRadivalue",Float32,queue_size=10)
pub4 =rospy.Publisher("pressure",Float32,queue_size=10)

def callback():
	alpharad = random.uniform(1,20)
	betarad = random.uniform(1,20)
	gamarad = random.uniform(1,20)
	pre = random.uniform(1000,1600)
	pub1.publish(alpharad)
	pub2.publish(betarad)
	pub3.publish(gamarad)
	pub4.publish(pre)
def talker():
	
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		callback()
		rate.sleep()
	rospy.spin()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
