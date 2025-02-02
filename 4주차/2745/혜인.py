N, B_str = input().split()
list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
B = int(B_str)
total = 0
b = int(len(N)) 
for i in range(0,b):
    c = b - i - 1
    a = N[c]
    list_index = list.index(a)
    total += ((B ** i) *  list_index)

print(total) 
