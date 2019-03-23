def pancake_sort(lst):
	for size in reversed(range(len(lst))):
		max_ind = max_pos(lst[:size + 1])
		print('Before\t\t', lst)
		reverse(lst, 0, max_ind)
		print('First flip\t\t', lst)
		reverse(lst, 0, size)
		print('Second flip\t\t', lst)
		
def max_pos(lst):
	return lst.index(max(lst))

def reverse(lst, i, j):
	while i < j:
		lst[i], lst[j] = lst[j], lst[i]
		i += 1
		j -= 1

lst = [1,5,3,4,2]
pancake_sort(lst)
