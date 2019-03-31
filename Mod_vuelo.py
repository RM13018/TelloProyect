from djitellopy import Tello
import cv2
import time

tello = Tello()
tello.connect()
tello.takeoff()
time.sleep(5)
tello.land()
time.sleep(5)
tello.end()

