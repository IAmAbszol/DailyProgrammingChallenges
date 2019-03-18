from random import randrange

'''
	Generating a number checking if its in k may lead to
	exponential time as a larger list would contain more values.

	Set intersection is perfect.
		
	n = 0 1 2 3 4 5
	k = 1 2 3 4 5
	n - k -> set = [0]
	pick from range 0 to len list
'''

def process(n, k):
	all_numbers = set([i for i in range(n)])
	set_k = set(k)

	return list(all_numbers - set_k)

def choose(n, k):
	if n < 0 or not k:
		return None
	my_list = process(n, k)
	return my_list[randrange(0, len(my_list))]

k = [1,2,3,4,5]
n = 4
for i in range(10):
	print(choose(n, k))
print("-"*50)
for i in range(10):
	print(choose(10, [1,2,3,4,5]))
