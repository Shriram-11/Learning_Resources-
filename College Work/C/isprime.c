#include<stdio.h>

int isprime(int n){
    int i;
    for(i=0;i<n/2;i++){
        if(n%2==0){
            return 0;
        }
    }
    return 1;
}

int main(){
    int n,r;
    printf("Enter a number: ");
    scanf("%d",&n);
    r=isprime(n);
    if(r==1){
        printf("Prime");
    }
    else{
        printf("Not Prime");
    }
}