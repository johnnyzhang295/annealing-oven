from simple_pid import PID
import math

temp = 73
sp = 100
pid = PID(1,.1, .1, setpoint=100)

error = pid(temp)
while (math.isclose(sp, temp) == False):
	error = pid(temp)
	temp = temp + error
	print(temp)

print("Last error value was")
print(error)
print("Final temp was")
print(temp)