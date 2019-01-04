def cons(a, b):
	def pair(f):
		return f(a, b)
	return pair

def car(pair):
	def grab(a, b):
		return a
	return pair(grab)

def cdr(pair):
	def grab(a, b):
		return b
	return pair(grab)

print(car(cons('a','b')))
print(cdr(cons('a','b')))
