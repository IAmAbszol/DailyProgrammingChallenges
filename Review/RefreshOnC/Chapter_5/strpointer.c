#include <stdio.h>

/* increment through pointing address to characters */
void strcpy(char *s, char *t)
{
	while ((*s = *t) != EOF)
	{
		s++;
		t++;
	}
}

void moar_strcpy(char *s, char *t)
{
	while(*s++ = *t++)
		;
}

int strcmp(char *s, char *t)
{
	for ( ; *s == *t; s++, t++)
	{
		if (*s == '\0')
		{
			return 0;
		}
	}
	return *s - *t;
}
