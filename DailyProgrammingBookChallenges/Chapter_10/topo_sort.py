'''
	Topological sort algorithm by Khan (Learned in my Data & Algorithms class in college.

	This algorithm uses a basic stack and will preprocess to find the intial start.

	We will take this value into our stack
	Pop that
	Add to result

	Take that value, look through all courses
	If that course contains our popped course
		Remove that course from the dict location
		if it becomes empty
			Add to stack
'''
