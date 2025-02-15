#include <stdio.h>
int main() {
    int i;
    scanf("%d", &i);//찾아야 하는 숫자 숫자
    int n = 1, j = 1;//n은 각 줄의 최댓값, j는 각 줄
    while (1) {
        if (n >= i)break;
        j++;//줄의 갯수 분석
        n = n + j;//줄의 최댓값 분석

    }
    if (j % 2 != 0) {//줄이 짝수일 경우 분자가 작은 수부터 시작
        printf("%d/%d", (n - i) + 1, j - (n - i));
    }
    else {//줄이 홀수일 경우 분자가 큰 수부터 시작
        printf("%d/%d", j - (n - i), (n - i)+1);
    }
    return 0;
}