def is_palindrome(ptr_a, ptr_b, s):
	while ptr_a >= 0 and ptr_b < len(s):
		if s[ptr_a] != s[ptr_b]:
			break
		ptr_a -= 1
		ptr_b += 1
	return [ptr_a + 1, ptr_b]

def palindrome(a):
	
	curr = [0, 1]
	for i in range(1, len(s)):
		odd_length = is_palindrome(i - 1, i + 1, a)
		even_length = is_palindrome(i - 1, i, a)
		curr_longest = max(odd_length, even_length, key=lambda x: x[1] - x[0])
		curr = max(curr_longest, curr, key=lambda x: x[1] - x[0])
	return s[curr[0]:curr[1]]
	
