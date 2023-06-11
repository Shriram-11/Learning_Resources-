#include<stdio.h>
int main(){
    int n,d,r=0,c=0;
    printf("Enter a number:");
    scanf("%d",&n);
    while(n!=0){
        d=n%10;
        r=r*10 + d;
        c++;
        n/=10;
    }
    printf("No. of digits:%d\n Reverse of the number:%d\n",c,r);
    return 0;
}