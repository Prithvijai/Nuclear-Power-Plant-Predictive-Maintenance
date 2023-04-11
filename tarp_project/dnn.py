import rospy
import numpy as np
import tensorflow as tf
from pushbullet import Pushbullet
from std_msgs.msg import String, Float32MultiArray


API_KEY = "o.dbb6zr91Dzv7vbZER528t573v5vialgO"

pb = Pushbullet(API_KEY)


class DNNNode:

    def my_callback(self, msg):
        my_array = msg.data
        print('Received array:', my_array)
        input_value = np.array([my_array])
        output = self.model.predict(input_value)
        print('Output:', np.rint(output))
        # Publish the output to the 'dnn_output' topic
        output_msg = String()
        output_msg.data = str(np.rint(output[0][0]))
        self.pub.publish(output_msg)
        output_int = np.rint(output)
        if(output_int[0][1]==1):
        	push = pb.push_note("Alert","coolent need maintenance")
        if(output_int[0][2]==1):
        	push = pb.push_note("Danger","Total breakdown going happen please cheack motor and reactant")

    def __init__(self):
        # Initialize ROS node
        rospy.init_node('dnn_node', anonymous=True)

        # Load the pre-trained model
        self.model = tf.keras.models.load_model('tarp_model.h5')

        # Define publisher for output
        self.pub = rospy.Publisher('dnn_output', String, queue_size=10)

        # Define subscriber for input
        self.sub = rospy.Subscriber('dnndata', Float32MultiArray, self.my_callback)

        # Start ROS loop
        rospy.spin()

if __name__ == '__main__':
    node = DNNNode()

	




    
