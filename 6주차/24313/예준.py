import sys

def f(a1, a0, n0):
    return a1*n0 + a0
def g(c, n0):
    return c*n0

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())
# a0, a1이 0보다 크든 작든 c보다 클 경우 무조건 부등호 방향이 바뀐다.
# 예를 들어 4n - 3 <= 3n (n>=1)
# 수식을 정리하면 3 >= n (n>=1) --> [1,3] 으로 
# n>=n0인 모든 경우에서 성립하지 않는다.
if f(a1,a0,n0) <= g(c,n0) and a1 <= c:
    print(1)
else:
    print(0)
