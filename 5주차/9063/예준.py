lix = []
liy = []

n = int(input())

for i in range(n):
    x,y = map(int, input().split())
    lix.append(x)
    liy.append(y)

print((max(lix)-min(lix))*(max(liy)-min(liy)))
