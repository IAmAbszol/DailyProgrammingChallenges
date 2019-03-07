#include <stdio.h>

int main()
{
	int a[] = { 1, 2, 3, 4, 6 };
	
	int *p = &a[0];
	int x = *p;
	printf("%d\n", x);
	printf("%d, %d\n", x, a[0]);
	*p = 5;
	printf("%d, %d\n", x, a[0]);
	p += 1;
	*p = 10;
	printf("%d\n", a[0]);	
	printf("%d\n", a[1]);	
}
