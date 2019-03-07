import unittest

def find_max(data):
	if data is None:
		return data
	string_list, coordinate_list = data
	condensed_string_list = list(set(string_list))
	count_list = [0 for i in range(len(condensed_string_list))]
	
	for point in coordinate_list:
		a, b = point
		idx = condensed_string_list.index(string_list[b])
		if idx == -1:
			print('What.')
			return None
		count_list[idx] += 1

	return max(count_list)

class Test(unittest.TestCase):

	data = [(('ABACA', [(0,1),(0,2),(2,3),(3,4)]), 3), (('A', []), None)]

	def test(self):
		for case, expected in self.data:
			actual = find_max(case)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
