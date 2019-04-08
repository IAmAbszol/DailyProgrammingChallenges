'''
	Perform a histogram approach using DP.

	This is like the house problem, instead we store all the results from
	the previous in the current row.

	Then we perform histogram analysis like the largest rectangle problem in a histogram.

	To fully explain.

	We start at the first row, calculate the solution or prev which then we run
	through largest area.

	Next when we go down, we pretty much increment the values along the way from previous.
	This in turn starts to form our "falling rectangle". If a rectangle of 2 by 3 from rows
	0 and 1 would have an accumulated sum of 2 with length of 3 on row 1.
	This falling aspect plays into this problem hard.

	Thinking about it further, if we view the problem at hand. Our rectangle lies in the middle.
	Any 1's accumulated and summed are going to show.
	This is why we use the histogram of the largest rectangle approach.

	By backtracking through our stack, we can calculate the run of this value backwards.
	Finally this value will be summed up to be our rectangles area.

	If we had the histogram 3 2 2 0. We could backtrack and draw this out as
	1 0 0 0
	1 1 1 0
	1 1 1 0

	This is exactly how this algorithm works. The run is any value of 2 or higher when on idx 2 (pos 3).

'''

def largest(histo):
	histo.append(0)
	stack = [-1]
	area = 0
	for i in range(len(histo)):
		while histo[i] < histo[stack[-1]]:
			# Calculate previous values. Think of this as a block. (Reason why 0 is on the end)
			# Backtrack through the stack and compare to our current index
			area = max(area, histo[stack.pop()] * (i - stack[-1] - 1))
		stack.append(i)
	return area	

def problem(matrix):
	if not matrix:
		return None

	# Houses problem implementation
	# Prev is the storage
	prev = matrix[0]
	area = max(0, largest(prev))
	for row in matrix[1:]:
		for i in range(len(row)):
			# Store previous to this
			if row[i] == 1:
				row[i] += prev[i]
		area = max(area, largest(row))
		print(prev, row)
		prev = row
	return area
			
print(problem([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]))
print(problem([[1,0,1,1,1],[0,0,0,0,0],[0,0,1,1,1],[0,0,0,0,0]]))
