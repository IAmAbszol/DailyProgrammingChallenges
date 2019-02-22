import random

import numpy as np
import sys

def toss_biased():
	bias = random.randint(0, 100)
	return 'H' if bias <= 10 else 'T'

# Before
results = []
for i in range(10000):
	results.append(toss_biased())
np_results = np.array(results)
unique, counts = np.unique(np_results, return_counts=True)
counts = [(count / 10000) for count in counts]
print(dict(zip(unique, counts)))

def toss_unbiased(data):
	'''
		T T T T T T H H H H
		.6 t
		.4 h
		Found occurnece was 30% h, if h above 30 percent
	'''

	lowest = None
	for i in data.keys():
		if not lowest in data.keys() or data[i] < data[lowest]:
			lowest = i
	
	generated = []
	for i in range(100):
		generated.append(toss_biased())
	np_generated = np.array(generated)
	unique, counts = np.unique(np_generated, return_counts=True)
	counts = [(count / 100) for count in counts]
	generated_dict = dict(zip(unique,counts))
	if generated_dict[lowest] > data[lowest]:
		return lowest
	else:
		other = list(set(data.keys()))
		other.remove(lowest)
		return other[0]

corrected_results = []
for i in range(10000):
	corrected_results.append(toss_unbiased(dict(zip(unique, counts))))
np_results = np.array(corrected_results)
unique, counts = np.unique(np_results, return_counts=True)
counts = [(count / 10000) for count in counts]	# Couldn't figure out why counts /= 10000 didn't apply as a scalar.
print(dict(zip(unique, counts)))
