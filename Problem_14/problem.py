from __future__ import division

import random

def monte_carlo():
	
	# Our circle - True --> Inside circle
	def circle(x, y):
		eq = x**2 + y**2
		if eq <= 1:
			return True
		return False

	def pi_calc(within, total):
		return 4 * (within / total)

	within_circle = 0
	total = 0

	for master in range(100000):
		for gen in range(1000):
			x, y = (random.randint(0, 100) / 100), (random.randint(0, 100) / 100)
			if circle(x, y):
				within_circle += 1
			total += 1

		print("Generation {}, PI = {}".format((master * gen), pi_calc(within_circle, total)))

monte_carlo()
