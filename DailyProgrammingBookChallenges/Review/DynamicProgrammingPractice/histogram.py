import sys

def problem(histo):
	h = len(histo)
	best = 0
	for i in range(1, h + 1):
		for j in range(0, h - i + 1):
			best = max(best, min(histo[j:j + i]) * i)
	return best
'''
	Use a stack, once we see a value less than the tail of our stack. Calculate.
	Take i - 1 as a base and compare to the end of the stack and the
	value torn off. If that value at the end is still < what were on currently.
	Calculate
	histogram location * how far back are we.

	say in the instance
	5 6 2
	5 6 are on the stack (index but displaying value) and we hit 2.
	Well at pos 2, we take the last item which was a 6 and go 1 step back,
	since this index has just hit.
	We obtain 6 by multiplying the histo[idx] = 6 * 1 [distance back].

	The next iteration is 5, this was two indices back from our current.
	Calculating 5 * (relative calculation) which is 2 --> 10. Thus 10.
	The next value is empty, thus we continue forward and add our index to the stack.

	In short, use the stack to backtrack indices until its not greater than our current or vice-versa (current < end of stack)
'''
def revised(histo):
	histo.append(0)
	histo.insert(0,0)
	best = 0
	stack = [0]
	for i in range(0, len(histo)):
		while histo[i] < histo[stack[-1]]:
			val = histo[stack.pop()] * (i - stack[-1] - 1)
			best = max(best, val)
		stack.append(i)
	return best

histo = [2,1,5,6,2,3]
print(revised(histo))
	
