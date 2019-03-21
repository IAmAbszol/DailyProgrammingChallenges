courses = {'CSC100': ['CSC300', 'CSC200'], 'CSC200': ['CSC300']}
for c in courses.get('CSC200', []):
	print(c)
