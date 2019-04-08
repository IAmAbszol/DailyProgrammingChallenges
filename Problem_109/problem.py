'''
	10101010 --> 01010101
	11100010 --> 11010001

	Swap even with odds
	Bit masking?
	
	10101010	01010101
	
	10101010 & above left --> 10101010 and shift to the right by 1
	Which results in
	01010101

	Same process above 
	11100010
	10101010
	--------
	10100010 >> 1 --> 01010001 (matches some of the part 2 solution)

	Maybe odds as well?
	
	11100010
	01010101
	--------
	01000000 Shift to right causes it to not fill out the last bit.
	01000000 << 1 --> 1000000

	01010001
	10000000
or	--------
	11010001 --> boom
'''

def problem(bits):
	return (bits & 0b10101010) >> 1 | (bits & 0b01010101) << 1
