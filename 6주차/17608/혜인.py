import sys

N  = int(sys.stdin.readline())
N_list = []
total = 1

for _ in range(N):
    N_list.append(int(sys.stdin.readline()))

max1 = N_list[-1]

for i in range(N-2, -1, -1):
    if max1 < N_list[i]:
        max1 = N_list[i]
        total += 1
print(total)