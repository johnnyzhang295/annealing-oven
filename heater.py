import RPi.GPIO as GPIO
import time

class Heater:
    channel_f = 23
    channel_h = 24
    
    def Setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel_f, GPIO.OUT)
        GPIO.setup(channel_h, GPIO.OUT)
        
        #Fan is always on
        GPIO.output(channel_f, GPIO.LOW)
        
    def On():
        GPIO.output(channel_h, GPIO.LOW)
        
    def Off():
        GPIO.output(channel_h, GPIO.LOW)