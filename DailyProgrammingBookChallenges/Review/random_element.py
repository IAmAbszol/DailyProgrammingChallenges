'''
	Pick a random element in a seemingly infinite stream.

	Each element has uniform probability if we consider the case that
	1/idx is the choice. Then for not being chosen, it would
	be 1 - i / (idx + 1) as (idx + 1) is the other.
	Thus multiplying the two results in 1/(idx + 1) which is our sampling.
'''

import random

def choose_random(stream):
	if stream is None:
		return None

	element = None
	for idx, item in enumerate(stream):
		if random.randint(1, idx + 1) == 1:
			element = item
	return element
