import random

def rand7():
	arr = [[1,2,3,4,5],
		   [6,7,1,2,3],
		   [4,5,6,7,1],
  		   [2,3,4,5,6],
		   [7,0,0,0,0]]
	
	x, y = rand5() - 1, rand5() - 1
	while arr[x][y] == 0:
		x, y = rand5() - 1, rand5() - 1
	return arr[x][y]

def rand5():
	return random.randint(1, 5)

for i in range(20):
	print(rand7())
