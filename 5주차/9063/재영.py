N = int(input())
a = []
b = []
for _ in range(N):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
print((max(a)-min(a))*(max(b)-min(b)))