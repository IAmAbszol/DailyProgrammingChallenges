import unittest
import itertools

def solve(k):
	if k < 0:
		return None
	pad = { 2:['a','b','c'],
			3:['d','e','f'],
			4:['g','h','i'],
			5:['j','k','l'],
			6:['m','n','o'],
			7:['p','q','r','s'],
			8:['t','u','v'],
			9:['w','x','y','z']
		  }
	pos = 10 * (len(str(k)) - 1)
	combos = []
	while pos >= 1:
		val = int(k / pos)
		k -= (pos * val)
		pos /= 10
		if not combos:
			combos = pad[val]
			continue
		combos = [zip(combos, pad[val]) for x in itertools.permutations(combos, len(pad[val]))][0]
	return [''.join(c) for c in combos]

class Test(unittest.TestCase):

	data =[(23, ['ad','ae','af','bd','be','bf','cd','ce','cf'])]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
