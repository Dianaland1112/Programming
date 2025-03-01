import sys

input = sys.stdin.readline

three = 0
five = 0

sugar = int(input())


while sugar > 0:
    if sugar % 5 == 0:
        five += sugar // 5
        break
    else:
        sugar -= 3
        three += 1

print(-1 if sugar < 0 else five + three)
