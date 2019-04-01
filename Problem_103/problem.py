def shortest(string, k):
	"""
		string --> figehaeci
		k	   --> {a, e, i}

		f	i	g	e	h	a	e	c	i
							^			^
		shortest --> aeci
		* Move right till set is within bounds.
		* Move left if only step 1 was satisfied.
	"""	

	if string is None or len(string) < len(k):
		return None

	left_ptr = 0
	right_ptr = len(k) - 1
	shortest_string = None
	while right_ptr < len(string):
		sub_string = string[left_ptr:right_ptr + 1]
		sub_set = set(list(sub_string))
		compare_set = set(k)
		if len(k) == len(sub_set - (sub_set - compare_set)):
			if shortest_string is None:
				shortest_string = sub_string
			else:
				if len(sub_string) < len(shortest_string):
					shortest_string = sub_string
			left_ptr += 1
		else:
			right_ptr += 1
	return shortest_string

print(shortest('figehaeci', ['a','e','i']))


