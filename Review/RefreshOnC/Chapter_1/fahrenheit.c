#include <stdio.h>

#define LOWER 0
#define UPPER 300
#define STEP 20

main()
{
	float fahr, celsius;
	int lower, upper, step;

	lower = LOWER;
	upper = UPPER;
	step = STEP;
	
	fahr = lower;
	// Exercise 1
	printf("This is a heading.\n");
	while (fahr <= upper)
	{
		celsius = (5.0/9.0) * (fahr - 32);
		// Extended 3 decimals on fahr and 6 on celsius with an extended decimal
		printf("%3.0f %6.1f\n", fahr, celsius);
		// Exercise 2
		float wereBack = 32 + (celsius)*(9.0 / 5.0);
		printf("Convereted %6.1f back to fahrenheit %3.0f.\n", celsius, wereBack);
		fahr += step;
	}
}
