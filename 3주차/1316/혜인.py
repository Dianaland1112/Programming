s = int(input())
total = s
for _ in range(s):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            total -=1
            breakpoint
print(total)

