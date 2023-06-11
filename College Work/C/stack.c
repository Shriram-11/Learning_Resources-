#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int top = -1, stack[101], top1 = -1;
char op[101];
void push(int n)
{
    stack[++top] = n;
}
void pushc(char n)
{
    op[++top1] = n;
}

char popc()
{
    return op[top1--];
}

int pop()
{
    return stack[top--];
}

int evaluate(int a, int b, char c)
{
    int r;
    if (c == '+')
        r = (a + b);
    else if (c == '-')
        r = (a - b);
    else if (c == '*')
        r = (a * b);
    else if (c == '/')
    {
        if (b == 0)
        {
            printf("Invalid\n");
            exit(0);
        }
        r = (a / b);
    }
    else
        r = 0;
    return r;
}
int value(char a)
{
    if (a == '+' || a == '-')
        return 1;
    else if (a == '*' || a == '/')
        return 2;
    else
        return 0;
}
void calc(char a)
{
    if (value(a) >= value(op[top1]))
    {
        pushc(a);
        return;
    }
    else
    {
        int a = pop();
        int b = pop();
        char c = popc();
        int r = evaluate(b, a, c);
        push(r);
        pushc(a);
    }
}

int main()
{
    char s[100];
    printf("Enter expression");
    scanf("%s", s);
    printf("Expression:%s\n", s);
    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/' || s[i] == ')' || s[i] == '(')
        {
            if (s[i] == '(')
            {
                pushc(s[i]);
            }
            else if (s[i] == ')')
            {
                while (op[top1] != '(')
                {
                    int a = pop();
                    int b = pop();
                    char c = popc();
                    int r = evaluate(b, a, c);
                    push(r);
                }
                popc();
            }
            else
            {
                calc(s[i]);
            }
        }
        else
        {
            int b = (int)s[i] - 48;
            push(b);
        }
    }
    printf("Result:%d\n", stack[top]);
    return 0;
}