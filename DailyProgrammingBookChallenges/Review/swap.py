import random

def shuffle(arr):
	
	for element in range(len(arr) - 1):
		idx = random.randint(element, len(arr) - 1)
		arr[element], arr[idx] = arr[idx], arr[element]
	return arr
