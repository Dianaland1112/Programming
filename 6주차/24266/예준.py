import sys

def MenOfPassion(n, A=[]):
    sum = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                sum += A[i] * A[j] * A[k]
    return sum

n = int(sys.stdin.readline())

print(n**3)
print(3)
