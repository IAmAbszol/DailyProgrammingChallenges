'''
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
'''

import unittest

def solve(arr, search):
	itineraries = {}
	path = []	

	def traverse(itir, arr, path, s):
		while s in itir.keys():
			# Bug bound here, fix by getting the index of the current key tuple and 
			# Mark arr[idx] = -1. When you recieve this tuple/going to,
			# ask if it's -1, if so, stop, we have completed the flight.
			if len(path) >= len(arr):
				break
			path.append(s)
			s = itir[s]
		return s
			
	for elm in arr:
		# Add the list element, were not to our search yet.
		itineraries[elm[0]] = elm[1]
		search = traverse(itineraries, arr, path, search)
	path.append(search)
	if len(path) < len(arr) + 1:
		return None
	return path

class Test(unittest.TestCase):

	data = [(([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'), ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']),
			(([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'), None),
			(([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'), ['A', 'B', 'C', 'A', 'C'])]

	def test(self):
		for case, expected in self.data:
			actual = solve(case[0], case[1])
			self.assertEquals(actual, expected)

if __name__=='__main__':
	unittest.main()
