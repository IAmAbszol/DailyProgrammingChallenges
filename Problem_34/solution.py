def is_palindrome(s):
	return s == s[::-1]

# O(2^n) time, overlaps for sure.
def make(s):
	if is_palindrome(s):
		return s
	'''
		If ends are the same, repeat making a palindrome by recursion
	'''
	if s[0] == s[1]:
		return s[0] + make(s[1:-1]) + s[-1]
	else:
		'''
			Form a palindrome around either end.
			The shortest one will be returned.
		'''
		left = s[0] + make(s[1:]) + s[0]
		right = s[-1] + make(s[:-1]) + s[-1]
		if len(left) < len(right):
			return left
		elif len(left) > len(right):
			return right
		else:
			return min(left, right)
		
cache = {}
def cache_make(s):
	# Don't proceed if the string we passed is already in cache. Hence
	# the reason for cache.
	if s in cache:
		print(cache)
		return cache[s]

	# If our string is a palindrome
	if is_palindrome(s):
		cache[s] = s
		return s
	# Store the compiled result for cache into slot s	
	if s[0] == s[-1]:
		result = s[0] + cache_make(s[1:-1]) + s[-1]
		cache[s] = result
		return result
	else:
		left = s[0] + cache_make(s[1:]) + s[0]
		right = s[-1] + cache_make(s[:-1]) + s[-1]
		cache[s] = min(left, right)
		return min(left, right)
 
print(cache_make('race'))
