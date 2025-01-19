n,m = map(int, input().split())
baskets =  [0]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    for i in range(a,b+1) :
        baskets[i] = c
for j in range(1, len(baskets)):
    print(baskets[j], end=' ')
