import sys

def problem(histo):
	h = len(histo)
	best = 0
	for i in range(1, h + 1):
		for j in range(0, h - i + 1):
			best = max(best, min(histo[j:j + i]) * i)
	return best

def revised(histo):
	histo.append(0)
	histo.insert(0,0)
	best = 0
	stack = [0]
	for i in range(0, len(histo)):
		print('Before while\t', stack, histo[i])
		while histo[i] < histo[stack[-1]]:
			print('In while\t', stack)
			best = max(histo[stack.pop()] * (i - stack[-1] - 1), best)
		stack.append(i)
	return best

histo = [2,1,5,6,2,3]
print(revised(histo))
	
