num=int(input())
beeH=1

for i in range(num):
    beeH += i*6
    if num <= beeH:
        print(i+1)
        break
