def recurse(x, y, m, n):
	if y == n - 1 and x == m - 1:
		return 1
	if x >= m:
		return 0
	if y >= n:
		return 0
	return recurse(x + 1, y, m, n) + recurse(x, y + 1, m, n)

def dp(m, n):
	subs = [[0 for i in range(m)] for i in range(n)]
	for i in range(m):
		subs[0][i] = 1
	for i in range(n):
		subs[i][0] = 1
	for i in range(1, n):
		for j in range(1, m):
			subs[i][j] = subs[i - 1][j] + subs[i][j -1]
	return subs[n - 1][m -1]

print(recurse(0, 0, 7, 3))
print(dp(7, 3))
