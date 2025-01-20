results = []
while (True):
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    results.append(A+B)
        
for i in range(len(results)):
    print(results[i])