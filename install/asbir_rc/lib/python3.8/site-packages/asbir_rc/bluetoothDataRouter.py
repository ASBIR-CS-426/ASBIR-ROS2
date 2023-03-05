#!/usr/bin/env python3
import evdev
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from pynput import keyboard

class TeleopGamePad(Node):
    def __init__(self):
            super().__init__('teleop-gamepad')
            self.ctrlPub = self.create_publisher(Int32MultiArray, 'servoControl', 1)
            self.controller = Int32MultiArray()
            self.controller.data = [1500, 1500, 1600, 1600]

            self.connectBluetooth()

            self.timer1 = self.create_timer(0.1, self.gamepadHandler)
            self.timer2 = self.create_timer(0.1, self.broadcast_timer_callback)

    def connectBluetooth(self):
        connecting = True
        while connecting:
            try:
                self.gamepad = evdev.InputDevice('/dev/input/event260')
                connecting = False
            except (FileNotFoundError, PermissionError):
                continue

    
    def broadcast_timer_callback(self):
        self.ctrlPub.publish(self.controller)

    def gamepadHandler(self):
        while rclpy.ok():
            try:
                event = self.gamepad.read_one()
                if event.type==3:
                    if event.code==4:
                        if event.value > 36000:
                            fw = 2400
                            bw = 2400
                        elif event.value < 28000:
                            fw = 800
                            bw = 800
                        else:
                            fw = 1600
                            bw = 1600
                    elif event.code==3:
                        if event.value < 28000:
                            fs = 1500-((32000-event.value)/32000)*(400)
                            bs = 1500+((32000-event.value)/32000)*(400)
                        elif event.value > 36000:
                            fs = 1500+((event.value-32000)/32000)*(400) 
                            bs = 1500-((event.value-32000)/32000)*(400)
                        else:
                            fs=1500
                            bs=1500
                    # print(ser.read())
            except (AttributeError):
                continue
            self.controller.data[0] = fs
            self.controller.data[1] = bs
            self.controller.data[2] = fw
            self.controller.data[3] = bw

            print(fs, bs, fw, bw)

def main(args=None):
    rclpy.init(args=args)
    node = TeleopGamePad()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
