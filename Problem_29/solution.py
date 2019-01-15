import unittest

def solve(case):
	'''
		AABBCCD
		A, 1
		A = iter.next()
		A, 2
		A != iter.next()
		Result append (2A)	
		B, 1 ....
	'''
	if case is None or not case or not all([c.isalpha() for c in case]):
		return None

	iterator = iter(list(case))
	character, count = 0, 0
	resultant = ""
	while True:
		try:
			tmp = next(iterator)
			if character == 0:
				character, count = tmp, 1
				continue
			if tmp == character:
				count += 1
			else:
				resultant += "{}{}".format(count, character)
				character, count = tmp, 1
		except:
			resultant += "{}{}".format(count, character)
			break
	return resultant


class Test(unittest.TestCase):

	data = [("AAAABBBCCDAA", "4A3B2C1D2A"),
			("AABBCCYY", "2A2B2C2Y"),
			("", None)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
