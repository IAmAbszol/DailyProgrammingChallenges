import unittest

def solve(string):
	if string is None:
		return None
	integer = None
	negative = False
	for c in string:
		if c in "-":
			negative = True
		if c.isnumeric():
			if integer is None:
				integer = 0
			integer = integer * 10 + int(c)
	return (-1 * integer) if negative else integer

class Test(unittest.TestCase):

	data =[(unicode("My int is 5, cool", "utf-8"), 5),
		   (unicode("My int is 515, cool", "utf-8"), 515),
		   (unicode("My int is abc, bad", "utf-8"), None),
		   (unicode("Forgot negatives, -5151, whoops!", "utf-8"), -5151)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()

	
