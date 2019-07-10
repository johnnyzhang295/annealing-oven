from pid import PID
import math

temp = 157
sp = 100
pc = PID(.25, 0, 0, 100)

error = pc(temp)
while (math.isclose(sp, temp) == False):
	error = pc(temp)
	temp = temp + error
	print(temp)

print("Last error value was")
print(error)
print("Final temp was")
print(temp)