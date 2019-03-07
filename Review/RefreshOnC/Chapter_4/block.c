#include <stdio.h>

int main()
{
	int i = 10;
	if (i < 11)
	{
		int i = 12;
		printf("%d\n", i);
	}
	printf("%d\n", i);
}
