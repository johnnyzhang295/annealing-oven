import numpy as np
import matplotlib.pyplot as plt

class Ramp:
	def __init__(self, time_end=100, max_temp=240, min_temp=20):
		profile = np.array([np.arange(0,time_end,.5), np.arange(min_temp,max_temp,1)])

	def draw(self):
		plt.plot(self.profile)