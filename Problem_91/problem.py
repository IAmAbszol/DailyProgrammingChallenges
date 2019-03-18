functions = []
for idx, i in enumerate(range(10)):
	functions.append(lambda x: i)

for f in functions:
	print(f(0))
