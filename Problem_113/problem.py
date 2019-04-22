'''
	Hello world here --> Here world hello

	This one isn't too bad, we just
	1. Reverse the entire string
	2. Once space or end of string, swap from last to curr.
'''

def swap(string):

	if string is None:
		return

	# Step 1
	string = string[::-1]
	
	# Step 2
	splits = string.split(' ')

	res = ''
	for idx, e in enumerate(splits):
		res += e[::-1] + (' ' if idx < len(splits) - 1 else '')
	return res	

print(swap('hello world here'))
