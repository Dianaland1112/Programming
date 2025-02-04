import sys

input = sys.stdin.readline


n = int(input())

password = []

for i in range(n):
    password.append(input().strip())


for i in range(n):
    for j in range(i, n):
        if password[i][::-1] == password[j]:
            width = len(password[i])
            print(f"{len(password[i])} {password[i][width//2]}")
            exit()
