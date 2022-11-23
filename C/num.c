
#include <stdio.h>
int main(int argc, char **argv)
{
    int a, b, i;
    scanf("%d%d", &a, &b);
    char arr[] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    for (i = a; i <= b; i++)
    {
        if (i >= 0 && i < 10)
        {
            printf("%s\n", arr[i]);
        }
        else
        {
            if (i % 2 == 0)
            {
                printf("evem\n");
            }
            else
            {
                printf("odd\n");
            }
        }
    }
    return 0;
}