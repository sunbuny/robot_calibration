import rosbag

with rosbag.Bag('output_arm.bag', 'w') as outbag:
    for topic, msg, t in rosbag.Bag('calibration_poses.bag').read_messages():
        # This also replaces tf timestamps under the assumption 
        # that all transforms in the message share the same timestamp
        #print 'convert a message'
        msg.features.append("gripper_finder")
        outbag.write(topic, msg, t)