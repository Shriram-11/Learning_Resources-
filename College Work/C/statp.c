#include<stdio.h>
#include<math.h>
int main(){
    int n;
    float m,s=0,sd=0,std;
    printf("Enter the size of the array:");
    scanf("%d",&n);
    int a[n],*p=a;
    printf("Enter array elements:");
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(int i=0;i<n;i++){
        s+=*p;
        p++;
    }
    m=s/n;
    p=a;
    for(int i=0;i<n;i++){
        sd+=pow((*p)*m,2);
        p++;
    }
    std=sqrt(sd/n);
    printf("Sum:%f\nMean:%f\nStandard deviation:%f",s,m,std);
}