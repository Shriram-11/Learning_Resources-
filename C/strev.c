#include<stdio.h>
#include<stdlib.h>
int main(){
    int i,j=0;
    char s[1024],t;
    printf("Enter a string:");
    gets(s);
    for(i=0;s[i]!='\0';i++){
    }
    i--;
    while(j<i){
        t=s[j];
        s[j]=s[i];
        s[i]=t;
        i--;
        j++;
    }
    printf("Reversed string: %s",s);
    return 0;
}
