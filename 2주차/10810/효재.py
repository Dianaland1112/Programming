N, M = map(int, input().split())
basket = [0] * N

for num in range(M):
    i, j, k = map(int, input().split())
    for index in range(i-1, j):
        basket[index] = k

print(*basket)