a = input('')
word.append(a)
n = 0
for i in range(len(a)):
    list1 = []
    if word[i] not in list1:
        b = word[i]
        list1.append(b)        
    else:
        if word[i] != (word[i - 1] or word[i + 1]):
            n = n - 1
print (n)
