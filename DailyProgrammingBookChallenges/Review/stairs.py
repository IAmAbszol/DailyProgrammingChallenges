def staircase(n):
	if n < 0:
		return None

	cache = [ 0 for i in range(n + 1) ]

	cache[0] = 1

	for i in range(1, n + 1):
		cache[i] = sum(cache[i - step] for step in [1,2])
	return cache[n]

print(staircase(2))
