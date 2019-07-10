import RPi.GPIO as GPIO
import time

class Heater:
    
    def __init__(self):
        channel_f = 23
        channel_h = 24

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel_f, GPIO.OUT)
        GPIO.setup(channel_h, GPIO.OUT)

        power = GPIO.PWM(channel, frequency)
        
        #Fan is always on
        GPIO.output(channel_f, GPIO.LOW)
        
    def On(self):
        GPIO.output(self.channel_h, GPIO.LOW)
        self.power.start(0)
        
    def Off(self):
        GPIO.output(self.channel_h, GPIO.LOW)

    def PWM(self, duty_cycle):
        self.power.ChangeDutyCycle(duty_cycle)
