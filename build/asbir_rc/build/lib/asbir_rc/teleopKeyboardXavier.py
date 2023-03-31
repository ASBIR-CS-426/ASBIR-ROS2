#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from pynput import keyboard

class Teleop(Node):
    def __init__(self):
            super().__init__('teleopKeyboard')
            self.ctrlPub = self.create_publisher(Int32MultiArray, 'servoControl', 1)
            self.controller = Int32MultiArray()
            self.controller.data = [50, 50, 50, 50]

            self.listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
            self.listener.start()

            self.timer = self.create_timer(0.1, self.broadcast_timer_callback)
    
    def broadcast_timer_callback(self):
        self.ctrlPub.publish(self.controller)

    def on_press(self,key):
        try:
            if key.char == "w":
                self.controller.data[2]=75
                self.controller.data[3]=25
            elif key.char == "s":
                self.controller.data[2]=25
                self.controller.data[3]=75
            elif key.char == "a":
                self.controller.data[0]=25
                self.controller.data[1]=75
            elif key.char == "d":
                self.controller.data[0]=75
                self.controller.data[1]=25
        except AttributeError:
            # print(key)
            print(self.controller.data)

        self.ctrlPub.publish(self.controller)

    def on_release(self,key):
        try:
            if key.char == "w":
                self.controller.data[2]=50
                self.controller.data[3]=50
            elif key.char == "s":
                self.controller.data[2]=50
                self.controller.data[3]=50
            elif key.char == "a":
                self.controller.data[0]=50
                self.controller.data[1]=50
            elif key.char == "d":
                self.controller.data[0]=50
                self.controller.data[1]=50
        except AttributeError:
            # print(key)
            print(self.controller.data)
    
        self.ctrlPub.publish(self.controller)

def main(args=None):
    rclpy.init(args=args)
    node = Teleop()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()