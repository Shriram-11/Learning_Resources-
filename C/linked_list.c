#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};
struct Node *head;

void Print()
{
    struct Node *temp = head;
    while (temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

void Insert(int x)
{
    struct Node *temp = (struct Node *)malloc(sizeof(struct Node));
    temp->data = x;
    temp->next = NULL;
    if (head != NULL)
        temp->next = head;
    head = temp;
    Print();
}

void top()
{
    struct Node *temp = head;
    if (temp != NULL)
        printf("%d ", temp->data);
    else
        printf("Stcak empty\n");
}

void pop()
{
    struct Node *temp;
    if (head == NULL)
        return;
    temp = head;
    head = temp->next;
    free(temp);
}

int main()
{
    struct Node *head = NULL;
    int i, x, n;
    printf("\nEnter no. of elements:");
    scanf("%d", &n);
    printf("Enter numbers one by one:");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &x);
        Insert(x);
        /*Print();*/
    }
    printf("\n");
    Print();
    pop();
    Print();
    return 0;
}