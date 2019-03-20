'''
    Books solution 
    Wasn't quite explained that well along with a lack of understanding
    on a few parts.
'''

import heapq
from collections import defaultdict

def compute_similiarity(a, b, visitors):
    # Quick and easy way to choose smallest and highest for num/den
    return len(visitors[a] & visitors[b]) / len(visitors[a] | visitors[b])

def top_pairs(log, k):
    visitors = defaultdict(set)
    for site, user in log:
        visitors[site].add(user)

    pairs = []
    sites = list(visitors.keys())

    for _ in range(k):
		# Fill heap with values higher than 0, gets poped then pushed.
        heapq.heappush(pairs, (0, ('', '')))

    for i in range(len(sites) - 1):
        for j in range(i + 1, len(sites)):
			# Iterate over 
            score = compute_similiarity(sites[i], sites[j], visitors)
            heapq.heappushpop(pairs, (score, (sites[i], sites[j])))

    return [pair for pair in pairs]

sites = [ ('www.google.com', 1),('www.google.com', 3),('www.google.com', 5),
          ('pets.com', 1), ('pets.com', 2), ('yahoo.com', 6),
          ('yahoo.com', 2), ('yahoo.com', 3), ('yahoo.com', 4),
          ('yahoo.com', 5), ('wiki.org', 4), ('wiki.org', 5), ('wiki.org', 6),
          ('wiki.org', 7), ('bing.com', 1), ('bing.com', 3), ('bing.com', 5),
          ('bing.com', 6)]

print(top_pairs(sites, 3))
