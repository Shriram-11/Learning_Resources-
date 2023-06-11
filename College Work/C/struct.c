#include<stdio.h>
struct empl{
    char name[64];
    int id;
    char branch[64];
    float sal;
};

int main(){
    struct empl e[64];
    int i,n;
    printf("Enter no. of employees:");
    scanf("%d",&n);
    printf("Enter employee details");
    for(i=0;i<n;i++){
        printf("Enter in form (name id branch sal\n)");
        scanf("%s%d%s%f",e[i].name,&e[i].id,e[i].branch,&e[i].sal);
    }

    printf("Details entered are:\n");
    printf("Name\tId\tBranch\tSalary\n");
    for(i=0;i<n;i++){
        printf("%s\t%d\t%s\t%f\n",e[i].name,e[i].id,e[i].branch,e[i].sal);
    }
}