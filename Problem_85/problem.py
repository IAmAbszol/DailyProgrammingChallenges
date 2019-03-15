'''
	Bit-wise operations
	x = 32bit int, lets say 5
	y = 32bit int, lets say 10
	b = 1 --> x else 0 --> y
	we should full mask if b is 1
	b = -1 will obtain a full bit mask of 0xFFFFFFFF
	To obtain either x or y
	x & b returns x as any 0 within x will be trashed from b.
	y & ~b returns y. We perform 2s complement on b
'''

def what_is(x, y, b):
	return (x & b) | (y & ~b)

print(what_is(5, 10, 0))
print(what_is(5, 10, 1))
