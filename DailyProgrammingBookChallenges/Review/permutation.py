def permutation(n, k):
	if k < 1:
		return n
	def next_perm(n):
		def reverse(n, a, b):
			n[a:b+1] = reversed(n[a:b+1])
		pivot = len(n) - 2
		while pivot >= 0 and n[pivot] >= n[pivot + 1]:
			pivot -= 1

		if pivot >= 0:
			must_swap = len(n) - 1
			while must_swap > 0 and n[must_swap] <= n[pivot]:
				must_swap -= 1
			n[must_swap], n[pivot] = n[pivot], n[must_swap]
		reverse(n, pivot + 1, len(n) - 1)
		return n

	for i in range(k):
		n = next_perm(n)
	return n

print(permutation([1,2,3], 0))
print(permutation([1,2,3], 1))
print(permutation([1,2,3], 2))

	
