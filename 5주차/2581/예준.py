M = int(input())
N = int(input())

prime = []

for i in range(M, N+1):
    if i > 1:
        prime.append(i)
        for j in range(2, i):
            if i%j == 0:
                prime.remove(i)
                break

if len(prime) != 0:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)
