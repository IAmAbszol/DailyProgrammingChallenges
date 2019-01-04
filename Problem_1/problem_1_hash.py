import sys

the_list = list(map(int, sys.argv[1].split(",")))
k = 17

dict_table = {}

for i in the_list:
	if i in dict_table.keys() and i == (k - i):
		print(i, i)
		exit(0)
	if (k - i) in dict_table.keys() and dict_table[(k - i)] == i:
		print(i, (k-i))
	dict_table[i] = (k - i)

print("Completed")
	
