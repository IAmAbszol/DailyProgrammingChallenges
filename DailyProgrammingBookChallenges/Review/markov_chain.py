'''
	This problem is from the book to demonstrate a Markov chain,
	this being a chain of sequenced probabilities.
'''

from collections import defaultdict
from random import random

def transform(states):
	d = defaultdict(dict)
	for start, end, prob in states:
		d[start][end] = prob
	return d

def choose_next(state, probs):
	choice = random()
	for possible, prob in probs[state].items():
		choice -= prob
		if choice <= 0:
			return possible

def markov(start_state, states, steps):
	probability = transform(states)
	count = defaultdict(int)
	current_state = start_state
	for i in range(steps):
		count[current_state] += 1
		current_state = choose_next(current_state, probability)
	return count

chain = [
	('a','a',0.9),
	('a','b',0.075),
	('a','c',0.025),
	('b','a',.15),
	('b','b',.8),
	('b','c',.05),
	('c','a',.25),
	('c','b',.25),
	('c','c',.5)
	]

print(markov('a', chain, 1000))
