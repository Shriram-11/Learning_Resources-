#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};
struct Node *head;

struct Node *Print(struct Node *head)
{
    struct Node *temp = head;
    while (temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
    return head;
}

struct Node *Insert(struct Node *head, int x)
{
    struct Node *temp = (struct Node *)malloc(sizeof(struct Node));
    temp->data = x;
    temp->next = NULL;
    if (head != NULL)
        temp->next = head;
    head = temp;
    return head;
}

struct Node *Reverse(struct Node *head)
{
    struct Node *current, *prev, *next;
    current = head;
    prev = NULL;
    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
}
int main()
{
    struct Node *head = NULL;
    Insert(head, 1);
    Insert(head, 2);
    Insert(head, 3);
    Insert(head, 4);
    Insert(head, 2);
    Insert(head, 1);
    Insert(head, 3);
    Print(head);
    Reverse(head);
    Print(head);
    return 0;
}

// output 1 2 3 4 5