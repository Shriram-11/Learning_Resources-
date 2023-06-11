#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
    FILE *f1,*f2;
    char c,ch,s[1024];
    f1=fopen("ip.txt","w");
    f2=fopen("op.txt","w");
    printf("Enter in lower case:");
    gets(s);
    fprintf(f1,"%s",s);
    fclose(f1);
    f1=fopen(" D:/C programs/ip.txt","r");
    fscanf(f1,"%s",s);
    for(int i=0;s[i]!='\0';i++){
        c=toupper(s[i]);
        if(c==' ' && ch==c){
            continue;
        }
        putc(c,f2);
        ch=c;
    }
    printf("Done\n");
    fclose(f1);
    fclose(f2);
}