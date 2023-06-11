#include<stdio.h>
int main(){
    int a[1024],n,i,j,t;
    printf("Enter size of the array: ");
    scanf("%d",&n);
    printf("Enter array elements:");
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++){
        for(j=0;j<n-i;j++){
            if (a[j]>a[j+1]){
                t=a[j];
                a[j]=a[j+1];
                a[j+1]=t;
        }
    }
    }
    printf("Sorted array:");
    for(j=0;j<n;j++){
        printf("%d ",a[j]);
    }
}