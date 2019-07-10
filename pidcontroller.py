import time
from simple_pid import PID

class PIDController:
	
    def __init__(self, kp=1.0, ki=0.0, kd=0.0, setpoint=100.0, output_limits=(20,240)):
        pid = PID(Kp=kp, Ki=ki, Kd=kd, setpoint=setpoint, output_limits=output_limits)
     
    def __call__(self, input_):
    	return self.pid(input_)
    	 
    def tune(self, kp=0.0, ki=0.0, kd=0.0):
    	self.pid.tunings = (kp, ki, kd)

    def setPoint(self, setpoint_value):
    	self.pid.setpoint = setpoint_value

