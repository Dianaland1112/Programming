import sys
# int 를 사용하면 개행문자 \n 사라짐
n = int(sys.stdin.readline())
sticks = []
ans = 0
mx = 0

for _ in range(n):
    sticks.append(int(sys.stdin.readline()))

for stick in reversed(sticks):
    if stick > mx:
        mx = stick
        ans += 1
        
print(ans)
