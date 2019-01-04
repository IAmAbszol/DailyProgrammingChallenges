def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
        print(cache)
    return cache[n]

print(staircase(5, [1,3,5]))

def traverse_staircase(n, X):
	# Create a cache of possibilities, +1 for base case
	cache = [0 for i in range(n + 1)]
	cache[0] = 1
	for i in range(1, n+1):
		# Cache represents if we had only n many steps within the i-ith range
		# Hence evaluating X[sub] to i, can we make this move?
		cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
	return cache[n]
