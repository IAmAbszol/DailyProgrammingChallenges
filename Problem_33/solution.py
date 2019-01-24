from __future__ import division
import unittest

# 2 1 5 7 2 0 5
# 1 	2	5	7
# 2 	1.5 2	3.5
# O(n^2) time complexity with O(n) space.
# Time complexity is O(n) for streaming and worst case O(n) for backtracking 
# for insertion sort.
# Introduce maxheap for better performance. 
def solve(arr):
	if arr is None or len(arr) <= 1:
		return arr
	
	medians = []
	streaming = []
	for elm in arr:
		streaming.append(elm)
		for j in range(len(streaming) - 1, 0, -1):
			count += 1
			if streaming[j] > streaming[j - 1]:
				break
			tmp = streaming[j - 1]
			streaming[j - 1] = streaming[j]
			streaming[j] = tmp
		if len(streaming) % 2 == 1:
			idx = int(len(streaming) / 2)
			medians.append(streaming[idx])
		else:
			idx = int(len(streaming) / 2)
			avg = (streaming[idx] + streaming[idx - 1]) / 2
			medians.append(avg)			
	return medians

class Test(unittest.TestCase):
	
	data = [([2,1,5,7, 2, 0, 5], [2, 1.5, 2, 3.5, 2, 2, 2])]
	def test(self):
		for case, expected in self.data:
			actual = solve(case)
			self.assertEquals(actual, expected)

if __name__ == '__main__':
	unittest.main()
