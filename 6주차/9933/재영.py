N = int(input())
list =[]
result=[]
for i in range(N):
    a = input()
    list.append(a)
for i in range(N):
    reverse_a = list[i][::-1]
    if reverse_a in list:
        result.append(reverse_a)
    else:
        pass
print(len(result[0]),result[0][len(list[0])//2])