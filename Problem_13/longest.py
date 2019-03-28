def longest_substring(s, k):
	if k == 0:
		return 0

	bounds = (0,0)
	h = {}
	max_length = 0

	for i, char in enumerate(s):
		h[char] = i
		print(h, bounds)
		if len(h) <= k:
			new_lower = bounds[0]
		else:
			key_pop = min(h, key=h.get)
			new_lower = h.pop(key_pop) + 1
		bounds = (new_lower, bounds[1] + 1)
		max_length = max(max_length, bounds[1] - bounds[0])
	return max_length

print(longest_substring('abcba', 2))
