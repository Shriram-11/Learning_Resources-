#include <stdio.h>
#include <string.h>

#define max 100
int top = -1, stack[max], stack2[max];

void push(char x)
{

    if (top == max - 1)
    {
        printf("stack overflow");
    }
    else
    {
        stack[++top] = x;
    }
}

char pop()
{
    return stack[top--];
}

int main()
{
    char str[max];
    char str2[max];
    int len = strlen(str);
    printf("Enter a string:");
    gets(str);
    int i;

    for (i = 0; str[i] != '\0'; i++)
        push(str[i]);

    for (i = 0; i < len; i++)
        str2[i] = pop();
    if (strcmp(str, str2) == 0)
    {
        printf("Pallindrome");
    }
    else
    {
        printf("Not a pallindrome");
    }
    return 0;
}