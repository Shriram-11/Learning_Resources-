#include<stdio.h>
#include<string.h>
int main(){
    char s[1024],o;
    int i,j=0,c=0;
    printf("Enter a string:");
    gets(s);
    printf("Enter a character: ");
    scanf("%c",&o);
    for(i=0;s[i]!='\0';i++){
        if(s[i]==o){
            c++;
            continue;
        }
        s[j]=s[i];
        j++;
    }
    s[j]='\0';
    printf("Occurences of %c:%d\n Updated string:%s",o,c,s);

}