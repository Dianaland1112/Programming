import sys

def MenOfPassion(n, A=[]):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += A[i] * A[j]
    return sum

n = int(sys.stdin.readline())

print(n*n)
print(2)
