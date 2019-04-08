def fib(n, cache={}):
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n in cache:
		return cache[n]
	else:
		val = fib(n - 2) + fib(n - 1)
		cache[n] = val
		return val

def dp(n):

	if n <= 1:
		return n
	
	fib = [0, 1]
	while len(fib) <= n:
		fib.append(0)

	if fib[n - 1] == 0:
		fib[n - 1] = dp(n - 1)
	if fib[n - 2] == 0:
		fib[n - 2] = dp(n - 2)
	fib[n] = fib[n - 1] + fib[n - 2]
	return fib[n]
		

print(fib(2))	# 0 1 = 1
print(fib(9))	# 0 1 1 2 3 = 3

print(dp(2))
print(dp(9))
