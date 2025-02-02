N,M = map(int,input().split())
result = []
for i in range(N):
    result.append(0)
for i in range(M):
    a,b,c = map(int,input().split())
    for j in range(a-1,b):
        result[j]=c
for k in range(N):
    print(result[k],end=' ')