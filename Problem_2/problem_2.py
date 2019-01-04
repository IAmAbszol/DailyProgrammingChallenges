import sys

my_list = list(map(int, sys.argv[1].split(",")))
eval_list = []
for i in range(len(my_list)):
	sum = 1
	for j in range(len(my_list)):
		if i != j:
			sum *= my_list[j]
	eval_list.append(sum)
print(eval_list)

# O(n^2)

# Try to solve in nlogn or best n
