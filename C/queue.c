#include <stdio.h>
#include <stdlib.h>
#define max 5
int rear = -1, front = -1, q[max];

void enq(int x)
{
    if ((rear + 1) % max == front)
    {
        printf("Full\n");
        return;
    }
    else if (rear == -1 && front == -1)
        front = rear = 0;
    else
        rear = (rear + 1) % max;
    q[rear] = x;
}

void deq()
{
    if (rear == -1 || front > rear)
    {
        printf("Empty\n");
    }
    else if (front == rear)
    {
        printf("Deleted %d", q[front]);
        front = rear = -1;
    }
    else
    {
        printf("Deleted %d", q[front]);
        front = (front + 1) % max;
    }
}

void display()
{
    printf("\n---------------------------\n");
    for (int i = front; i <= rear; i++)
        printf(" %d\n", q[i]);
}

int main()
{
    for (int i = 0; i < 5; i++)
        enq(i);
    display();
    deq();
    display();
    display();
    return 0;
}