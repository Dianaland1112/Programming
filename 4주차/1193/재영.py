x=int(input())
i=1
if x ==1 :
    print('1/1')
else:
    while x>=1:
        x = x-i
        i +=1
    if i%2 ==1:
        a = i-1+x
        b = i-a
    else:
        b = i-1+x
        a = i-b
    print('%d/%d' %(a,b))
