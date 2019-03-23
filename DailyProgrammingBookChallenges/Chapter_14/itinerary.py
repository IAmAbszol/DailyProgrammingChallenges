def get_itinerary(flights, current):
	if not flights:
		return current
	last_stop = current[-1]
	for i, (origin, destination) in enumerate(flights):
		other_flights = flights[:i] + flights[i + 1:]
		current.append(destination)
		if origin == last_stop:
			return get_itinerary(other_flights, current)
		current.pop()
	return None

print(get_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'),('YUL','YYZ'),('HKO','ORD')], ['YUL']))
