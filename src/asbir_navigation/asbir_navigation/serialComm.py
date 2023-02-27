#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

import serial


class SerialComm(Node):
    def __init__(self):
        super().__init__('serialComm')
        self.tfBuffer = Buffer()
        self.tfListener = TransformListener(self.tfBuffer, self)
        self.ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)
        
        self.servoSub = self.create_subscription(Float32MultiArray, 'servoControl', self.servoSubCallback, 1)

    def servoSubCallback(self, msg):
        self.ser.write('{} {} {} {}'.format(msg.data[0],msg.data[1],msg.data[2],msg.data[3]))
        print('{} {} {} {}'.format(msg.data[0],msg.data[1],msg.data[2],msg.data[3]))

def main(args=None):
    rclpy.init(args=args)
    node = SerialComm()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
