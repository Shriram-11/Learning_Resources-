#include<stdio.h>

void fact(int n, int *f)
{
    int i;
    *f=1;
    for(i=1; i<=n; i++)
        *f=*f*(i);


}
int main()
{
    int i,n,f;
    printf("Enter a number:");
    scanf("%d",&n);
    fact(n,&f);
    printf("Factorial of %d is %d",n,f);
}
