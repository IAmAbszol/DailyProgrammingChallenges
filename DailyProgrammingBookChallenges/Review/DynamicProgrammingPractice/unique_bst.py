def count(n, cache={}):
	if n <= 1:
		return 1

	if n in cache:
		return cache[n]

	total = 0
	for i in range(n):
		left = count(i)
		right = count(n - i - 1)
		total += left * right
		cache[n] = total
	return total

print(count(3))
