#include <stdio.h>
#include <stdlib.h>

int main(char **argv, int argc) {

	int size = 100;
	int *arr = (int *)malloc(size * sizeof(int));
	
	int i = 0;
	int n = 2;

	// Array creation
	for(i = 0; i < size; i++, n++) {
		arr[i] = n;
	}


	// Sieve
	for(i = 0; i < size; i++) {
		if(arr[i] == -1) {
			continue;
		}
		n = arr[i];
		int j = 2;
		for(j = 2; j < size; j++) {
			if(n * j > (size + 1)) {
				break;
			}
			arr[(n * j) - 2] = -1;
		}
	}


	// Print array
	for(i = 0; i < size; i++) {
		if(arr[i] != -1) {
			fprintf(stdout, "%d\n", arr[i]);
		}
	}

	return 0;

}
