#include<stdio.h>
int main(){
    int r=0,n,m,d;
    printf("Enter a number: ");
    scanf("%d",&n);
    m=n;
    while(n!=0){
        d=n%10;
        r+=(d*d*d);
        n/=10;
    }
    if(m==r){
        printf("Armstrong no.");
    }
    else{
        printf("Not an Armstrong no.");
    }
}