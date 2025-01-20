N, M = map(int, input().split())
results = []

for i in range(N):
    results.append(i+1)
    
for _ in range(M):
    i, j = map(int, input().split())
    results[i-1:j] = reversed(results[i-1:j])

print(*results)