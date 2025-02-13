import sys
ans =[]

# set에는 순서가 없다
sys.stdin.readline()
N = set(map(int, sys.stdin.readline().split()))

sys.stdin.readline()
M = list(map(int, sys.stdin.readline().split()))

# M에는 순서가 필요하다. 하지만 N은 i의 존재여부만 판단하면 된다.
for i in M:
    if i in N:
        ans.append('1')
    else:
        ans.append('0')

print(' '.join(ans))
