#include<stdio.h>
int main()
{
    int m,n,p,q,r,gcd,lcm;
    printf("Enter two numbers:");
    scanf("%d%d",&p,&q);
    m=p;
    n=q;
    r=m%n;
    while(r!=0)
    {
        m=n;
        n=r;
        r=m%n;
    }
    gcd=n;
    lcm=p*q/n;
    printf("GCD:%d\nLCM:%d",gcd,lcm);
    return 0;
}