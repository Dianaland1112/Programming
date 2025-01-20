results=[0]*30
for i in range(28):
    n = int(input())
    results[n-1] = n

for i in range(30):
    if results[i] != i+1:
        print(i+1)