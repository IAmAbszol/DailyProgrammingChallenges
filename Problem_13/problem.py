def longest(string, k):
	# Simple base case
	if k > len(string):
		return string

	# End the search of k elements to start off with
	start = 0
	ending = 2
	
	# Best string yielded
	best = ""	

	# Exhuast in O(n) time 
	while ending < len(string):

		sub_string = list(string[start:ending+1])

		# We moved too much forward, move up the tail
		if len(set(sub_string)) > k:
			start += 1
		# Our move was justified. Evaluate and move ending forward.
		elif len(set(sub_string)) <= k:
			if len(best) < len(sub_string):
				best = ''.join(sub_string)
			if ending < len(string):
				ending += 1

	return best


print(longest('acabbb', 2))
