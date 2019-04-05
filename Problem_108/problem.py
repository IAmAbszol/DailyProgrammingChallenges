'''
	A	->	abcdefg
	B	->	cbefgab
'''
# Runs in O(n) time but suffers from a problem of amazon --> azonam.
def problem(a, b):
	if a is None or b is None or len(a) != len(b) or len(a) < 1:
		return False
	if len(a) < 2:
		return a[0] == b[0]
	
	ptr_a = 0
	ptr_b = 0
	
	while a[ptr_a] != b[ptr_b]:
		ptr_b += 1
		if ptr_b >= len(b):
			return False

	while ptr_a < len(a):
		if a[ptr_a] != b[ptr_b % len(b)]:
			return False
		ptr_a += 1
		ptr_b += 1
	
	return True

print(problem('abc','cab'))
print(problem('abc','cba'))

	
