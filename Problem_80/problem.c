#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	char data;
	struct node *left;
	struct node *right;
} Node;

typedef struct tree {
	struct node *root;
	int level;
} Tree;

struct node *createNode(char data);
void printTree(struct tree t);
int depth(struct node n);

int main(int argc, char **argv) 
{

	struct node *a = createNode('a');
	struct node *b = createNode('b');
	struct node *c = createNode('c');
	struct node *d = createNode('d');

	struct tree *myTree = (struct tree *) malloc(sizeof(struct tree));

	a->left = b;
	a->right =c;
	b->left = d;

	return 0;
}

void printTree(struct tree t)
{
	
}

struct node *createNode(char data)
{
	struct node *node = (struct node *) malloc(sizeof(struct node));
	node->data = data;
	
	node->left = NULL;
	node->right = NULL;

	return node;
}
