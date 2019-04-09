'''
	s1 - aabcc
	s2 - dbbca
	s3 - aadbbcbcac
	true

	Plan of action:
	Using DP
	s1 will be the rows
	s2 will be the columns

	if the current rows previous is true and our value to s3 is true
	[i + j - 1] --> Positional to s2[j - 1], then that should yield the interleave.

	Same with s1 and s3, swap j with i.

	aab bcd --> aabbcd

	0	b	c	d
0	T	F	F	F
a	T	F	F	F
a	T	T	F	F
b	T	T	T	T

i consults above solution
j consults to the left solution

We can condense this into single rows of building solutions, keeping a precomputed previous
'''

def problem(s1, s2, s3):

	m = len(s1)
	n = len(s2)

	if m + n != len(s3):
		return

	# Construct array
	prev = [True]

	for i in range(0, n):
		prev.append(s2[i] == s3[i])

	for i in range(1, m + 1):
		curr = [prev[0] and s1[i - 1] == s3[i - 1]]
		for j in range(1, n + 1):
			res = (curr[-1] and s2[j - 1] == s3[i + j - 1]) or (prev[j] and s1[i - 1] == s3[i + j - 1])
			curr.append(res)
		prev = curr
		print(curr)
	return prev[-1]

print(problem('aab','bcd','aabbcd'))
print(problem('adb','aabbc','aaabbdbc'))
