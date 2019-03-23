def tower(n, a='1', b='2', c='3'):
	'''
		This solution can be seen as moving our top block to the end (c).
		Then we will switch the spare as c and our target as b. Thus moving
		our second block in the recursive sequence to b. (target).
		Finally we will swap again and say our a is the spare, b is the starter
		and c is the target. (After finishing recursive sequence.
	'''
	if n >= 1:
		tower(n - 1, a, c, b)
		print('Moving {} to {}.'.format(a, c))
		tower(n - 1, b, a, c)
