#include <stdio.h>
int main(){
    int find;
    scanf("%d",&find);
    int i=1;
    int range=1;
    while(1){
        if(range>=find){
            break;
        }
        range=range+i*6;
        i++;
    }
    printf("%d",i);
    return 0;
}