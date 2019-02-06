import random

def problem(arr, k):
	
	def rand(k):
		return random.randint(1, k)

	for idx in range(0, len(arr), 2):
		k_idx = rand(k)
		arr[idx], arr[k_idx] = arr[k_idx], arr[idx]

	return arr

# Each idx maps to a card in actual implementation
my_deck = [i for i in range(52)]
print(my_deck)
print(problem(my_deck, 52))
