'''
	This is the disjoint problem, though I'm doing it quite differently.

	This problem can be summarized as a Union-find algorithm implementation.

	1. Initialze an array of length k, where k is an integer representing the number of students.
	2. Set the elements of the array to -1.
	
	Add : Student 3 is friends with 5
	1. Look at Student 3, is it -1? 
		Yes: Change -1 to 5
		No: Implementation detail: Follow path till -1, meaning we hop to each index pointed to till -1.
		Change that index to 5.
		OR
		Change 5 to point to 3's parent. 
		For this problem I'll choose the second choice as we don't care about the insertion, just the quick 
		identification of -1s (How many diverse friend groups).

	How many friends
	Sum([1 for i in arr if i == -1]) --> Number of friend groups

	0	1	2	3	4	5	6
	-1	0	0	-1	-1	0	3
	
	Thus 3 diverse friend groups.
'''
