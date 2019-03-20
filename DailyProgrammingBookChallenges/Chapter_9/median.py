'''
	Calculate the running median of a streamed array (Unknown length, etc)

	Original method I came up with:
		Insertion sort, calculate median by len(arr) // 2 or evaluate mid + r / 2

	Book solution, pretty cool:
		Max/min heaps

		If our streamed value is > median, place in min to control that side
		Else max heap
	
		Keep leveling diff, if there off by more than 1, rebalance the respected heap

	*I've never used heapq, great learning experience
	Note: Heaps can actually just reside in an array, running
	heapify on an existing array will... heapify it.

	Left side node of a heap is 2i + 1
	RHS is 2i + 2

'''

import heapq

def get_median(min_heap, max_heap):
	if len(min_heap) > len(max_heap):
		min_val = heapq.heappop(min_heap)
		heapq.heappush(min_heap, min_val)
		return min_val
	if len(min_heap) < len(max_heap):
		max_val = heapq.heappop(max_heap)
		heapq.heappush(max_heap, max_val)
		return max_val
	min_val = heapq.heappop(min_heap)
	heapq.heappush(min_heap, min_val)

	max_val = heapq.heappop(max_heap)
	heapq.heappush(max_heap, max_val)

	return (min_val + max_val)  / 2

def add(x, min_heap, max_heap):
	if len(min_heap) + len(max_heap) == 1:
		heapq.heappush(max_heap, x)
		return

	median = get_median(min_heap, max_heap)
	if x < median:
		heapq.heappush(max_heap,x)
	else:
		heapq.heappush(min_heap,x)
	
def rebalance(min_heap, max_heap):
	# Could also difference and use abs() built-in function
	if len(min_heap) > len(max_heap) + 1:
		val = heapq.heappop(min_heap)
		heapq.heappush(max_heap, val)
	elif len(max_heap) > len(min_heap) + 1:
		val = heapq.heappop(max_heap)
		heapq.heappush(min_heap, val)

def print_median(min_heap, max_heap):
	print(get_median(min_heap, max_heap))

def running_median(stream):
	min_heap = []
	max_heap = []
	for num in stream:
		add(num, min_heap, max_heap)
		rebalance(min_heap, max_heap)
		print_median(min_heap, max_heap)
		
