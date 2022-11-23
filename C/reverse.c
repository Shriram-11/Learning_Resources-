#include <stdio.h>
#include <stdlib.h>
#define max 100
int top = -1, stack[max], arr[max];
void display()
{
    printf("\n---------------------------\n");
    printf("Stack:\n");
    for (int i = top; i >= 0; i--)
    {
        printf("%d\n", stack[i]);
    }
    printf("\n---------------------------\n");
}
void push(int x)
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
void reverse()
{
    printf("\n---------------------------\n");
    for (int i = 0; i <= top; i++)
        printf("%d\n", stack[i]);
    printf("\n---------------------------\n");
}
char pop()
{
    return stack[top--];
}

int main()
{
    int a, ch, b[max], c = 0, i;
    while (1)
    {
        printf("\n1. Push\n2. Pop\n3. Reverse\n4. Display\n5. Exit\nEnter choice:");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            printf("\nEnter:");
            scanf("%d", &a);
            push(a);
            c++;
            break;
        case 2:
            printf("Deleted %d", pop());
            c--;
            break;
        case 3:
            printf("Original stack");
            display();
            printf("\n");
            printf("Reversed stack:");
            reverse();
            /*for (i = 0; i < c; i++)
                printf("%d ", pop());
            printf("\n");*/
            break;
        case 4:
            display();
            break;
        case 5:
            exit(0);
            break;
        default:
            printf("Invalid input");
            break;
        }
    }
    return 0;
}