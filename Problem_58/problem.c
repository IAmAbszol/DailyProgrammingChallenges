#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(char **argv) {

	/*
		Cases
		
		0. None --> [1,2,3,4,5] --> [1,2,3,4,5]
		LHS of mid is < mid and RHS of mid is > mid.		
	
		1. Rotate right --> [1,2,3,4,5] --> [4,5,1,2,3]
		LHS of mid is > mid and RHS of mid is < mid.

		2. Rotate left --> [1,2,3,4,5] --> [3,4,5,1,2]
		LHS of mid is < mid and RHS of mid is < mid

		[1,2,3,4,5]
		start = 0
		mid = 2
		end = 4
		Find 4
		val mid < val end
			start = mid + 1
			mid = start + high / 2
		val mid == ans 

		[4,5,1,2,3]
		start = 0
		mid = 2
		end = 4
		Case 1
		val start >= val mid
			k >= val start amd k <= val mid
				high = mid - 1
				continue
			else
				low = mid + 1
			continue
		Case 2
		val start < val mid
			if k >= val start and k <= val mid
				high = mid - 1
			else
				low = mid + 1
	*/

	int arr[] = { 13, 18, 25, 2, 8, 10 };
	int high = sizeof(arr) / sizeof(int);
	fprintf(stdout, '%d

	return 0;

}
