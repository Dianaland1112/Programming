import sys
input = sys.stdin.readline

stick = []
n = int(input())

for _ in range(n):
    height = int(input())
    stick.append(height)

cnt = 1
max_height = stick[-1]

for i in range(n-2, -1, -1):
    if stick[i] > max_height:
        cnt += 1
        max_height = stick[i]

print(cnt)