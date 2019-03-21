'''
	Dict { 
			CSC300 : [CSC200, CSC100]
			CSC200 : [CSC100]
			CSC100 : []
		}

	courses = []
			

'''

# Topological sort problem
def courses_to_take(course_to_prereqs):
    # Copy list values into a set for faster removal.
    course_to_prereqs = {c: set(p) for c, p in course_to_prereqs.items()}

	# Check what the base is, what needs no requirements	
    todo = [c for c, p in course_to_prereqs.items() if not p]

    # Used to find courses D which have C as a prerequiste
	# Other words, just match our course to what has it as a prerequiste
    prereq_to_coures = {}
    for course in course_to_prereqs:
        for prereq in course_to_prereqs[course]:
            if prereq not in prereq_to_coures:
                prereq_to_coures[prereq] = []

            prereq_to_coures[prereq].append(course)
    print(prereq_to_coures)
    result = [] # courses we need to take in order

    while todo:
        prereq = todo.pop()
        result.append(prereq)

        # Find which courses are now free to take
        for c in prereq_to_coures.get(prereq, []):
            print(c, prereq)
            course_to_prereqs[c].remove(prereq)
            if not course_to_prereqs[c]:
                todo.append(c)

    # Cicrcular dependency
    if len(result) < len(course_to_prereqs):
        return None
    return result

courses = {'CSC300' : ['CSC200', 'CSC100'],
		   'CSC200' : ['CSC100'],
		   'CSC100' : []}
print(courses_to_take(courses))
