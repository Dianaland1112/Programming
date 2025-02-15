#include <stdio.h>
int draw(int (*white)[101], int a, int b) {
    int sum = 0;
    for (int j = 100 - b; j > 90 - b; j--) {
        for (int i = a; i < a + 10; i++) {
            if (white[j][i] == 0) {
                white[j][i] = 1;
                sum++;
            }
            
        }
    }
    return sum;
}

int main() {
    int white[101][101] = { 0 };
    int count, a, b;
    scanf("%d", &count);
    int sum=0; // 색칠한 블록 갯수 세기
    for (int i = 0; i < count; i++) {
        scanf("%d %d", &a, &b);
        sum+=draw(white, a, b);
    }
    printf("%d", sum);
}