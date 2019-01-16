import unittest

def solve(arr):
	
	i = 0
	j = len(arr) - 1
	
	l_max = 0
	r_max = 0
	
	water_held = 0

	while i <= j:
		# Evaluate left as this side depends on how much water is to be held
		# 3, 1, 5
		if arr[i] < arr[j]:
			if arr[i] < l_max:				
				water_held += l_max - arr[i]
			else:
				l_max = arr[i]
			i += 1
		# 5, 1, 3. Can't overfil on 3.
		else:
			if arr[j] < r_max:
				water_held == r_max - arr[j]
			else:
				r_max = arr[j]
			j -= 1
	return water_held
				

class Test(unittest.TestCase):

	data = [([3, 0, 1, 3, 0, 5], 8)]

	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
