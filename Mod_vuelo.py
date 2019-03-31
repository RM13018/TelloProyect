from djitellopy import Tello
import cv2
import time

tello = Tello()

def tello_control():
    tello.takeoff()
    time.sleep(5)
    tello.land()
    time.sleep(5)
    tello.end()

def main():
    tello.connect()
    tello_control()
if __name__ == '__main__':
    main()