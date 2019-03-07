#include <stdio.h>

void swap(int *x, int *y);

int main()
{
	int x = 1, y = 2, z[10];
	int *ip;
	// Address of x
	ip = &x;
	// What *ip was pointing to, this case being x
	y = *ip;
	// Change to 0, indirectly changing x to 0 =O
	*ip = 0;
	// Ip now points to address of z[0]
	ip = &z[0];

	// add one to what ip is pointed to
	y = *ip + 1;

	printf("%d, %d\n", x, y);
	swap(&x, &y);
	printf("%d, %d\n", x, y);

}

void swap(int *x, int *y)
{
	int temp;

	temp = *x;
	*x = *y;
	*y = temp;
}
