import numpy as np
import matplotlib.pyplot as plt

class Ramp:
	def __init__(self, fname):
		self.loadProgrammable('anneal_plastic.txt')

		self.ramp_up_time = self.anneal_presets[self.material][0]
		self.setpoint = self.anneal_presets[self.material][1]
		self.__hold_time = self.anneal_presets[self.material][2]
		self.cool_rate = self.anneal_presets[self.material][3]

		self.soak_period = self.determineSoakPeriod()
		self.profile = self.createRampProfile()

	def determineSoakPeriod(self):
		if self.thickness < 6:
			#If thickness is less than 6mm or 1/4", return minimum soak time
			return self.__hold_time * 1
		else:
			#If thickness is greater than 6mm or 1/4", return (soak time per 6mm) 
			return self.__hold_time * (self.thickness//6)

	def createRampProfile(self):
		#ramp up time, cool rate are intially in hours
		ramp_up = np.linspace(0, self.setpoint, self.ramp_up_time*60)
		hold = np.full((self.soak_period,), self.setpoint)
		cooling = np.arange(self.setpoint, 0, -(self.cool_rate/60))

		total_time = self.ramp_up_time*60 + self.soak_period + cooling.size
		x_axis = np.linspace(0, total_time/60, total_time)
		y_axis = np.concatenate((ramp_up, hold, cooling))

		return np.array([x_axis, y_axis])

	def plot(self):
		plt.plot(self.profile[0], self.profile[1])

	def loadProgrammable(self, fname):
		self.material = np.loadtxt(fname, dtype=str, usecols=0).item()
		self.thickness = np.loadtxt(fname, dtype=int, usecols=1).item()

	def loadPresets(fname, endpoint):
		anneal_list = {}
		materials = np.loadtxt(fname, dtype=str, usecols=0)

		for index,row in enumerate(np.loadtxt(fname,dtype=int, usecols=range(1,endpoint))):
			anneal_list[materials[index]] = row

		return anneal_list

	anneal_presets = loadPresets('anneal_reference.txt', 5)