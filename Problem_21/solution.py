'''
	solution.py
	Classroom allocation problem.
	Attempting to solve in O(n) time.
	My attempt failed, though it is solvable in O(n) time.
	Geeks solution, instead of using tuple, separate into
	two separate lists. Makes sense.
'''

import unittest

def solve(times):
	count = 1
	total = 1
	times = zip(*times)
	arrival = list(times[0])
	departure = list(times[1])
	arrival.sort()
	departure.sort()
	start = 1
	ending = 0
	while start < len(arrival) and ending < len(arrival):
		if arrival[start] <= departure[ending]:
			count += 1
			start += 1
			if count > total:
				total = count
		else:
			ending -= 1
			count -= 1
	return total

class Test(unittest.TestCase):
	
	data = [(((0, 30), (15, 45), (60, 150), (60, 80), (90, 150)), 4),
			(((30, 75), (0, 50), (60, 150)), 2),
			(((30, 60), (45, 60), (60, 150)), 3)]
	
	
	def test_solution(self):
		for [case, expected] in self.data:
			actual = solve(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
