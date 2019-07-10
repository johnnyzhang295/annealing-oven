import time
from simple_pid import PID
import thermocouple
import heater

class PIDController:
	
    def __init__(self, kp=1.0, ki=0.0, kd=0.0, setpoint=100, output_limits=(20,240)):
        pid = PID(Kp=kp, Ki=ki, Kd=kd, setpoint=setpoint, output_limits=output_limits)
     
        
    def Update(self, input, output, controlled_system):
        while True:
            error = self.pid(input)
            
        	output = controlled_system.update(error)
    