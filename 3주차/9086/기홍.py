import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a = input().strip()
    f = 0
    last = len(a)-1
    print(f"{a[f]}{a[last]}")
