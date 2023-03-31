#!/usr/bin/env python

# Copyright (c) 2019-2022, NVIDIA CORPORATION. All rights reserved.
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import Jetson.GPIO as GPIO
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

# fsP = 32
# bsP = 33
fwP = 32
bwP = 33

GPIO.setmode(GPIO.BOARD)

# GPIO.setup(fsP, GPIO.OUT, initial=GPIO.HIGH)
# GPIO.setup(bsP, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(fwP, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(bwP, GPIO.OUT, initial=GPIO.HIGH)

# Steering Servo freq: 333hz
# fs = GPIO.PWM(fsP, 333)
# bs = GPIO.PWM(bsP, 333)


fw = GPIO.PWM(fwP, 50)
bw = GPIO.PWM(bwP, 50)


class SerialComm(Node):
    def __init__(self):
        super().__init__('serialComm')
        
        self.fsV = 50
        self.bsV = 50
        self.fwV = 50
        self.bwV = 50  

        # fs.start(self.fsV)
        # bs.start(self.bsV)
        fw.start(self.fwV)
        bw.start(self.bwV)
        
        self.timer = self.create_timer(0.2, self.broadcast_timer_callback)
        self.servoSub = self.create_subscription(Int32MultiArray, 'servoControl', self.servoSubCallback, 1)
        
    def broadcast_timer_callback(self):
        # fs.ChangeDutyCycle(self.fsV)
        # bs.ChangeDutyCycle(self.bsV)
        fw.ChangeDutyCycle(self.fwV)
        bw.ChangeDutyCycle(self.bwV)

    def servoSubCallback(self, msg):
        self.fsV = msg.data[0]
        self.bsV = msg.data[1]
        self.fwV = msg.data[2]
        self.bwV = msg.data[3]

def main(args=None):
    rclpy.init(args=args)
    node = SerialComm()
    rclpy.spin(node)

    fs.stop()
    bs.stop()
    GPIO.cleanup()

    node.destroy_node()
    rclpy.shutdown()

