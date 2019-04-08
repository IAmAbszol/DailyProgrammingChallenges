# Solution from modified Rabin Karp's algorithm. Keep completed list of any character.
# And compare to the patterns. This is identical to using a hashset and incrementing/decrementing.
def problem(string, pattern):

	def cmp(a, b):
		for i in range(len(a)):
			if a[i] != b[i]:
				return False
		return True

	CHARACTERS = 256
	m = len(string)
	n = len(pattern)
	result = []

	main_count = [0 for _ in range(CHARACTERS)]
	pattern_count = [0 for _ in range(CHARACTERS)]
	
	for i in range(n):
		main_count[ord(string[i])] += 1
		pattern_count[ord(pattern[i])] += 1

	for i in range(n, m):
		
		if cmp(main_count, pattern_count):
			# Back track to patterns initial start, not end.
			result.append(i-n)

		# Remove old
		main_count[ord(string[i-n])] -= 1

		# Update new
		main_count[ord(string[i])] += 1
		
	# Doesn't update last, check again to make up for it


	if cmp(main_count, pattern_count):
		result.append(m-n)
	
	return result
