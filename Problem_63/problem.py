import unittest

def solve(arr, s):
	if arr is None or s is None or not s:
		return None
	
	for r_idx, row in enumerate(arr):
		for c_idx, col in enumerate(row):
			ptr = 0
			if col == s[ptr]:
				c = c_idx + 1
				r = r_idx + 1
				ptr += 1
				while c <= len(row):
					if ptr >= len(s):
						return True
					if arr[r_idx][c] == s[ptr]:
						c += 1
						ptr += 1
					else:
						break
				ptr = 1
				while r <= len(arr):
					if ptr >= len(s):
						return True
					if arr[r][c_idx] == s[ptr]:
						r += 1
						ptr += 1
					else:
						break
	return False

arr = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

print(solve(arr, 'FOAM'))
print(solve(arr, 'MASS'))
print(solve(arr, 'DOG'))
