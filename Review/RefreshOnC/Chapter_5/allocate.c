#include <stdio.h>

#define ALLOCSIZE 10000

static char allocbuf[ALLOCSIZE];
static char *allocp = allocbuf;

char *alloc(int n)
{
	if (allocbuf + ALLOCSIZE - allocp >= n)
	{
		allocp += n;
		return allocp - n;
	}
	else
		return 0;
}

void afree(char *p)
{
	if (p >= allocbuf && p < allocbuf + ALLOCSIZE)
	{
		allocp = p;
	}
}

int main()
{
	printf("%d, %d\n", allocp, *allocp);
	char *mem = alloc(10);
	printf("%d, %d\n", allocp, *allocp);
	printf("%d, %d\n", mem, *mem);
}
