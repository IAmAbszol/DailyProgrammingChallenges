'''
	hello/world:here

	So for the two side cases, split wouldn't work unless we forcefully do so.

	Use pointers instead. Each side will have two pointers being
	left start, left end, right start, right end. 
	These pointers will creep until a delimiter is reached then swap from start to end + 1
	for Python splicing.

	hello//world:here
	^
	     ^
				-
					-
'''

def problem(s):
	delimiters = ['/',':'
