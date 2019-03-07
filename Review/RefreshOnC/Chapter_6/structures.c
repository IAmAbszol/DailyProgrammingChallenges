#include <stdio.h>

struct point {
	int x;
	int y;
};

struct rect {
	struct point pt1;
	struct point pt2;
};

struct point makepoint(int x, int y)
{
	struct point temp;

	temp.x = x;
	temp.y = y;
	return temp;
}

struct point addpoint(struct point p1, struct point p2)
{
	p1.x += p2.x;
	p1.y += p2.y;
	return p1;
}

main()
{
	struct rect screen;
	struct point middle;

	screen.pt1 = makepoint(0, 0);
	screen.pt2 = makepoint(100, 100);
	middle = makepoint((screen.pt1.x + screen.pt2.x) / 2,
					   (screen.pt1.y + screen.pt2.y) / 2);
}
