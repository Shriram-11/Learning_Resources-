#include <stdio.h>
#include<stdlib.h>
int main(){
    int a[1024],n,h,l,k,m;
    printf("Enter size of the array: ");
    scanf("%d",&k);
    printf("Enter array elements:");
    for(int i=0;i<k;i++){
        scanf("%d",&a[i]);
    }
    printf("Enter element to search:");
    scanf("%d",&n);
    h=k-1;
    l=0;
    while(l<=h){
        m=(l+h)/2;
        printf("%d: ",m);
        if(a[m]==n){
            printf("Found");
            exit(0);
        }
        else if(a[m]>n){
            h=m-1;
        }
        else{
            l=m+1;
        }

    }
    printf("Not found!");
    return 0;
}