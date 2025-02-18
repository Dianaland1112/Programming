import sys
input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n):
    words.append(input().strip())

for i in range(len(words)):
    if words[i] == words[i][::-1]:
        print(len(words[i]), words[i][(len(words[i])-1)//2])
        exit()
    for j in range(i+1, len(words)):
        if words[i] == words[j][::-1]:
            print(len(words[i]), words[i][(len(words[i])-1)//2])
            exit()