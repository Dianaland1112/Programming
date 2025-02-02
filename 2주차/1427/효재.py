results = []
n = int(input())
for digit in str(n):
    results.append(int(digit))
    results.sort(reverse=True)

for i in results:
    print(i, end='')