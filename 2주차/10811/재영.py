N,M = map(int,input().split())
result = []
for i in range(N):
    result.append(i+1)
for j in range(M):
    a,b = map(int,input().split())
    result[a-1:b] = result[a-1:b][::-1]
for i in range(N):
    print(result[i],end=' ')