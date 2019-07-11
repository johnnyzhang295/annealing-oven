import numpy as np

class Ramp:
	anneal_presets = {row[0]: row[1:] for row in (np.loadtxt('anneal_reference.txt', dtype=str))}

	def __init__(self, fname):
		self.material, self.thickness = np.loadtxt(fname, dtype=str)
		self.thickness = int(self.thickness)

		self.ramp_up_time = self.anneal_presets[self.material][0]
		self.setpoint = self.anneal_presets[self.material][1]
		self.hold_time = self.anneal_presets[self.material][2]
		self.cool_time = self.anneal_presets[self.material][3]

		self.soak_period = self.determineSoakPeriod()
		self.profile = self.createRampProfile()

	def determineSoakPeriod(self):
		if self.thickness < 6:
			#If thickness is less than 6mm or 1/4", return minimum soak time
			return self.hold_time * 1
		else:
			#If thickness is greater than 6mm or 1/4", return (soak time per 6mm) 
			return self.hold_time * (self.thickness//6)

	def createRampProfile(self):
		pass
