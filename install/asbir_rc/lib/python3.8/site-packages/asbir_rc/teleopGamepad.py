#!/usr/bin/env python3
import evdev
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class TeleopGamePad(Node):
    def __init__(self):
            super().__init__('teleopGamepad')
            self.ctrlPub = self.create_publisher(Int32MultiArray, 'servoControl', 1)
            self.controller = Int32MultiArray()
            self.controller.data = [1500, 1500, 1600, 1600]

            

            # self.timer = self.create_timer(0.1, self.broadcast_timer_callback) 
            self.gamepadHandler()
    
    def gamepadHandler(self):
        connecting = True
        while connecting:
            try:
                gamepad = evdev.InputDevice('/dev/input/event260')
                print('connected')
                connecting = False
            except (FileNotFoundError, PermissionError):
                print('connecting')

        print(gamepad)
        fs = 1500
        bs = 1500
        fw = 1600
        bw = 1600

        while True:
            event = gamepad.read_one()
            print(type(event))
            
            try:
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
            except (AttributeError):
                continue

            self.controller.data[0] = fs
            self.controller.data[1] = bs
            self.controller.data[2] = fw
            self.controller.data[3] = bw

            self.ctrlPub.publish(self.controller)

            

   
def main(args=None):
    rclpy.init(args=args)
    node = TeleopGamePad()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
