'''
	Given S and T, find the number of times
	we see T in S.

	S = rabbbit
	T = rabbit
	R = 3

	Rabin Karp algorithm?

	Map character code to index position, increment by 1 for each character.

	For c in T,
		max(c, current)

	
'''

def karp(s, t):

	MAX = 256

	# Build the array
	s_arr = [0 for i in range(MAX)]
	t_arr = [0 for i in range(MAX)]

	# Fill the array
	for c in s:
		s_arr[ord(c)] += 1

	for c in t:
		t_arr[ord(c)] += 1

	# Remove common elements
	for c in t:
		s_arr[ord(c)] -= 1
	
	# Setting it to one will include the base case of s = ab, t = ab
	total = 1
	for c in t:
		total += s_arr[ord(c)]

	return total

print(karp('rabbbit', 'rabbit'))
print(karp('babgbag', 'bag'))
