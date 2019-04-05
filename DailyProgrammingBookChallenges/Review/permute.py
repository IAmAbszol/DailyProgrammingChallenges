def problem(a, l, r):
	if l == r:
		print(a)
	else:
		for i in range(l, r + 1):
			a[i], a[l] = a[l], a[i]
			problem(a, l + 1, r)	
			a[i], a[l] = a[l], a[i]
problem(['A','B','C'], 0, 2)
