from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

import busio
import board
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import time

def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    pca = PCA9685(i2c)
    pca.frequency = 50

    fs = servo.Servo(pca.channels[12])
    bs = servo.Servo(pca.channels[13])
    fw = servo.ContinuousServo(pca.channels[14])
    bw = servo.ContinuousServo(pca.channels[15])

    fs.set_pulse_width_range(1000,2000)
    bs.set_pulse_width_range(1000,2000)
    fw.set_pulse_width_range(1460,1760)
    bw.set_pulse_width_range(1460,1760)

    # for i in range(90):
    #     fs.angle = i*2
    #     bs.angle = i*2
    #     time.sleep(0.1)
    for i in range(20):
        fw.throttle = (i-10)/10
        bw.throttle = (i-10)/10
        time.sleep(0.1)
    fs.angle=90
    bs.angle=90
    bw.throttle=0
    fw.throttle=0