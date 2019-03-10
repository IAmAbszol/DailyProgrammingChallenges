import itertools

from collections import defaultdict

def solve(n):
	if n < 2:
		return None

	phone = defaultdict(list)
	phone[2].append(['a','b','c'])
	phone[3].append(['d','e','f'])
	phone[4].append(['g','h','i'])
	phone[5].append(['j','k','l'])

	'''
		int(n / len(n)) --> dict access
		n -= dict access ^
	'''

	list_of_lists = []
	while int(n) > 1:
		base = (10 ** (len(str(n)) - 1))
		access = int(n / base)
		if access == 1:
			# Invalid request
			print("Invalid dict request.")
			return None

		list_of_lists.append(phone[access][0])
		n -= access * base

	return [r for r in itertools.product(*list_of_lists)]

print(solve(23))
print(solve(24))
print(solve(45))
print(solve(13))
print(solve(41))
