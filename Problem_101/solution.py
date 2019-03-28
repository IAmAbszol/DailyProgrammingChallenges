def sieve(n):
	
	if n < 2:
		return None	

	primes = []
	n -= 2
	for i in range(n):
		primes.append(i + 2)
	for i in range(n):
		if primes[i] == -1:
			continue
		elm = primes[i]
		for j in range(2, n):
			if elm * j > n + 1:
				break
			primes[(elm * j) - 2] = -1

	primes = [i for i in primes if i != -1]
	return primes

def solution(n):

	if n < 4:
		return None

	solutions = []
	primes = sieve(n)
	l = 0
	r = len(primes) - 1
	while l <= r:
		summed = primes[l] + primes[r]
		if summed == n:
			solutions.append((primes[l], primes[r]))
			l += 1
		elif summed < n:
			l += 1
		else:
			r -= 1
	return solutions[0]

print(solution(26))
print(solution(40))
print(solution(100))
print(solution(12))
print(solution(6))
