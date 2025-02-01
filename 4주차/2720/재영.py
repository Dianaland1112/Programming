N = int(input())
for _ in range(N):
    C = int(input())
    result = []
    result.append(C//25)
    result.append((C%25)//10)
    result.append(((C%25)%10)//5)
    result.append((C%5)//1)
    print(*result)