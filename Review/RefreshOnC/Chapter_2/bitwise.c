#include <stdio.h>

unsigned getbits(unsigned x, int p, int n);

int main()
{
	int n = 5;
	//n = n & 0177;
	printf("%d\n", n);

	printf("%d\n", getbits(n, 4, 3));
}

unsigned getbits(unsigned x, int p, int n)
{
	return (x >> (p + 1 - n)) & ~(~0 << n);
}
