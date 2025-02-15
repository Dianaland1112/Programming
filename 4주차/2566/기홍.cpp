#include <stdio.h>
int main(){
    int max=0,x,y;
    int a[9][9]={0};
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            scanf("%d",&a[i][j]);
            if(max<=a[i][j]){
                max = a[i][j];
                           x=i;
                           y=j;}
        }
    }
    printf("%d\n%d %d",max,x+1,y+1);
    return 0;
}