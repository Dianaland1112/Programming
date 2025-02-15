while (1):
    n = int(input())
    
    if n == -1:
        break
    
    divi_list = []
    for i in range(1,n):
        if n%i == 0:
            divi_list.append(i)
    
    if sum(divi_list) == n:
        print(f'{n} = {' + '.join(map(str, divi_list))}')
    else:
        print(f'{n} is NOT perfect.')
