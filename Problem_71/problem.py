import random

def rand7():
	return random.randint(1, 7)

def rand5():
	'''
	
		[[1,2,3,4,5]
		 [6,7,1,2,3]
		 [4,5,6,7,1]
		 [2,3,4,5,6]
		 [7,0,0,0,0]]
		
		[[1,2,3,4,5,6,7]
		[1,2,3,4,5,6,7]
		[1,2,3,4,5,6,7]
		[1,2,3,4,5,6,7]
		[1,2,3,4,5,6,7]
		[1,2,3,4,5,6,7]
		[1,2,3,4,5,6,7]]
	
		All have an equal chance of getting 1 - 7.
		If 6, 7, reroll
	
	'''
	rand5_choices = [[1,2,3,4,5,6,7],
		[1,2,3,4,5,6,7],
		[1,2,3,4,5,6,7],
		[1,2,3,4,5,6,7],
		[1,2,3,4,5,6,7],
		[1,2,3,4,5,6,7],
		[1,2,3,4,5,6,7]]
	
	r,c = rand7() - 1, rand7() - 1
	while rand5_choices[r][c] in {6,7}:
		r, c = rand7() - 1, rand7() - 1
	return rand5_choices[r][c]

counts = [0 for i in range(5)]
for i in range(1000):
	choice = rand5()
	counts[choice - 1] += 1

print(counts)

	
