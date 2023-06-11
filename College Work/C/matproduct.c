#include<stdio.h>
int main(){
    int m,n,p,q,i,j,k;
    printf("Enter order of matrix A as (m n)");
    scanf("%d%d",&m,&n);
    printf("Enter order of matrix B as (p q)");
    scanf("%d%d",&p,&q);
    int a[m][n],b[p][q],c[m][q];
    if(n==p){
        printf("Enter matrix a elements:"); //enter row wise//
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                scanf("%d",&a[i][j]);
            }
        }
        printf("Enter matrix b elements:");
        for(int i=0;i<p;i++){
            for(int j=0;j<q;j++){
                scanf("%d",&b[i][j]);
        }
        }
        for(int i=0;i<m;i++){
            for(int j=0;j<q;j++){
                c[i][j]=0;
                for(k=0;k<n;k++){
                    c[i][k]+=a[i][k]*b[k][j];
                }
            }
        }
        printf("Mat A*Mat b:\n");
        for(int i=0;i<m;i++){
            for(int j=0;j<q;j++){
                printf("%d ",c[i][j]);
            }
            printf("\n");
        }
    }
    else{
        printf("invalid input\n");
    }
}