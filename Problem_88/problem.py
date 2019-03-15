# Division with a twist --> No division, multiplication or modulous.
# We don't have to go into decimal land, only ints ... subtraction anyone

def problem(n, d):
	# Only positive ints.
	if n <= 0 or d <= 0:
		return None
	
	while d > 0:
		'''
			n = 10
			d = 2
			
			quotient
			10 -= 2 --> 1
			8 -= 2 --> 2
			6 -= 2 --> 3
			4 -= 2 --> 4
			2 -= 2 --> 5		
	
		'''
	

		quotient = 0
		while n >= d:
			n -= d
			quotient += 1
		return quotient

print(problem(10, 2))
print(problem(18, 7))
