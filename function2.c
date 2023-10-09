#include<stdio.h>
void printnamaste();
void printbonjour();

int main(){
    printf("enter i for indian and f for french");
    char ch;
    scanf("%c",&ch);
    if(ch=='i'){
        printnamaste();
    }
    else if(ch=='f'){
    printbonjour();
}
else{

printf("thanku");
}
return 0;
}
void printnamaste()
{
    printf("namaste\n");
}

void printbonjour(){
    printf("bonjour\n");
}