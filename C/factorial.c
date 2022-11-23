#include<stdio.h>
int fact(int n){
    if(n==0 || n==1){
        return 1;
    }
    return (n*fact(n-1));
}

int main(){
    int n,r,ncr,npr;
    printf("Enter n and r: ");
    scanf("%d%d",&n,&r);
    npr=fact(n)/fact(n-r);
    ncr=fact(n)/(fact(n-r)*fact(r));
    printf("nPr::%d\n ncr::%d\n",npr,ncr);
}