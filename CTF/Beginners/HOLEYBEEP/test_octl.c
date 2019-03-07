#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/ioctl.h>

int main() {
	int fd = open("test.txt", 0);
	printf("%d\n",ioctl(fd,0x4B2F,0));
	return 0;
}
