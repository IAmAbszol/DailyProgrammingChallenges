import unittest
from copy import deepcopy

def solve(arr):
	if arr is None:
		return arr

	lists = []
	for elm in arr:
		if not lists:
			lists.append([elm])
			continue
		# Case 1, create new list
		if all([elm < i[-1] for i in lists[:]]):
			lists.append([elm])
			continue
		# Case 2, largest element
		if all([elm > i[-1] for i in lists[:]]):
			# Clone largest and extend it
			ptr, largest_len = 0, 0
			for idx, ls in enumerate(lists):
				if len(ls) > largest_len:
					largest_len = len(ls)
					ptr = idx
			ls = deepcopy(lists[ptr])
			ls.append(elm)
			lists.append(ls)
			continue
		# Case 3, mid element
		ptr, largest_length = 0, 0
		for idx, ls in enumerate(lists):
			if len(ls) > largest_length and ls[-1] < elm:
				largest_length = len(ls)
				ptr = idx
		ls = deepcopy(lists[ptr])
		lists = [l for idx, l in enumerate(lists) if len(l) != (largest_length + 1)]
		ls.append(elm)
		lists.append(ls)
	longest = []
	for ls in lists:
		if len(ls) > len(longest):
			longest = ls
	return longest
		

class Test(unittest.TestCase):

	data = [([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15], [0,2,6,9,11,15])]
	
	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
