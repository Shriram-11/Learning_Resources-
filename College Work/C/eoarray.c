#include<stdio.h>
//replace even places by 0 and odd places by 1//
int main(){
    int a[1024],i,n;
    printf("Enter size of the array: ");
    scanf("%d",&n);
    printf("Enter array elements: ");
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }

    for(i=0;i<n;i++){
        if(i%2==0){
            a[i] = 0;
        }
        else{
            a[i] = 1;
        }
    }

    printf("Updated Array:");
    for(i=0;i<n;i++){
        printf("%d ",a[i]);
    }
}