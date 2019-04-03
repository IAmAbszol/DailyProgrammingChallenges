'''
	This problem requires the number of changes to change (minimum)
	word a to word b
	cat
	dog
	This would be 3
	cat
	fat
	This would be 1
	How about 
	taco
	cat
	This would be 3, from left to right as right to left would score 4.
'''
import sys

# Assumes equal length
#def distance(a, b):
#	return sum([ 0 if a[i] == b[i] else 1 for i in range(len(a)) ])

'''
def distance(a, b):
	if not a and not b:
		return 0
	if not a:
		return len(b)
	if not b:
		return len(a)
	if a[0] == b[0]:
		return distance(a[1:], b[1:])
	# If we proceed left, right or move up both. What causes a min?
	left = 1 + distance(a[1:], b)
	right = 1 + distance(a, b[1:])
	both = 1 + distance(a[1:], b[1:])
	return min(left, right, both)

def distance(d, a, b):
	if not a and not b:
		return 0
	if not a:
		return len(b)
	if not b:
		return len(a)
	
	if (a, b) not in d:
		if a == b:
			score = distance(d, a[1:], b[1:])
		else:
			left = 1 + distance(d, a[1:], b)
			right = 1 + distance(d, a, b[1:])
			both = 1 + distance(d, a[1:], b[1:])
			score = min(left, right, both)
		d[(a, b)] = score
	return d[(a, b)]
'''

def distance(a, b):
	m = len(a)
	n = len(b)
	table = [[ 0 for i in range(m + 1) ] for i in range(n + 1) ]
	
	for i in range(m + 1):
		table[0][i] = i
	for i in range(n + 1):
		table[i][0] = i

	for i in range(1, n + 1):
		for j in range(1, m + 1):
			if a[j - 1] == b[i - 1]:
				table[i][j] = table[i - 1][j - 1]
			else:
				table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
	return table[-1][-1]
		

print(distance('cat', 'dog'))
print(distance('fat', 'cat'))
print(distance('tacocat', 'cat'))
print(distance('cat', 'tacocat'))
