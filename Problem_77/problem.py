import unittest

def condense(arr):
	if arr is None:
		return arr
	'''
		ASSUMING THE INTERVAL IS COMPLETELY ENCLOSED/OVERLAPPED
		* What if (4,10), (5,12) --> would we say 4,12 or leave them separately?
		start, end = 0, 0
		s, e = 1, 3
		if e < new_s
		append s, e onto list

		s, e = 4, 10
		new_s = 5
		new_e = 8
		if e > new_e
			next elm		
	'''
	arr.sort()
	fixed = []
	for s, e in arr:
		if not fixed:
			fixed.append((s,e))
		if s <= fixed[-1][1]:
			prev_s, prev_e = fixed[-1]
			fixed[-1] = (prev_s, max(prev_e, e))
		else:
			fixed.append((s,e))
	return fixed


class Test(unittest.TestCase):

	data = [([(1,3),(5,8),(4,10),(20,25)], [(1,3),(4,10),(20,25)])]

	def test(self):
		for case, expected in self.data:
			actual = condense(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
