'''
	CSC100 : []
	CSC200 : [CSC100]
	CSC300 : [CSC200, CSC100]

	Khans method
	Extremely close to the solution but we use only preprocessing once
	as it's doable without the preqs to course list

	Let s be of Stack
	for each class, view requirements
		if requirements is None
			push class to s
	
	while s is not empty
		class = s.pop()
		result.append(class)

		for prereq in courses.keys():
			if class in courses[prereq] 
				delete class from course[prereq]
				if not course[prereq]
					push prereq to s
	if our result < courses
		return None
	
'''
def courses_to_take(courses):
	if courses is None:
		return None

	# Initialize our 'stack'
	s = []
	result = []

	# Obtain starting point
	for course in courses.keys():
		if not courses[course]:
			s.append(course)
	
	# Loop through all classes
	while s:
		course = s.pop()
		result.append(course)
		
		for prereq in courses.keys():
			if course in courses[prereq]:
				courses[prereq].remove(course)
				if not courses[prereq]:
					s.append(prereq)

	if len(result) < len(courses):
		return None
	return result
		

courses = {'CSC300' : ['CSC200', 'CSC100'],
		   'CSC200' : ['CSC100'],
		   'CSC100' : []}
print(courses_to_take(courses))
