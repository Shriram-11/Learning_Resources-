#include <stdio.h>
int top = -1, stack[101];
void push()
{
    int n;
    scanf("%d", n);
    stack[++top] = n;
}

void pop()
{
    if (top == -1)
    {
        printf("Empty Stack");
        return;
    }
    top--;
}

void print()
{

    if (top == -1)
    {
        printf("Empty Stack");
        return;
    }
    for (int i = top; i <= 0; i++)
    {
        printf(" %d ", stack[i]);
    }
}

int main()
{
    return 0;
}