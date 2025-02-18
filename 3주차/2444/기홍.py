n = int(input())
left = n
for i in range(1,n*2,2):
    left -= 1
    for j in range(left):
        print(' ',end="")
    for j in range(i):
        print('*',end="")
    print()
for i in range((n-1)*2-1,0,-2):
    left += 1
    for j in range(left):
        print(' ',end="")
    for j in range(i):
        print('*',end="")
    print()