# We'll use the bottom-up approach via a loop and cache
def staircase(n, X):
	if n < 0:
		return None

	# Build initial cache, last one will be answer
	cache = [0 for i in range(n + 1)]

	# Initial step is 1
	cache[0] = 1

	# Iterate through all, again last index is final
	for i in range(1, n + 1):
		cache[i] = sum(cache[i - step] for step in X if (i - step) >= 0)

	return cache[n]

print(staircase(4, [1,2]))
