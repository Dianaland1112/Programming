M = int(input())
N = int(input())

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

arr = []
for i in range(M, N+1):
    if is_prime(i):
        arr.append(i)
        
if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)