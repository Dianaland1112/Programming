T = int(input())
results = []

for _ in range(T):
    x = input()
    results.append(x)

for value in results:
    print(value[0] + value[-1])