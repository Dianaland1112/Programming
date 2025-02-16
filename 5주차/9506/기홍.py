def find_factor(num):
    _list = []
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            _list.append(i)
            sum += i

    result = True if sum == num else False
    return _list, result


while 1:
    a = int(input())
    if a == -1:
        exit()
    _list, result = find_factor(a)
    if result:
        print(f"{a} = ", end="")
        for i in _list[: len(_list) - 1]:
            print(f"{i} + ", end="")
        print(_list[len(_list) - 1])
    else:
        print(f"{a} is NOT perfect.")
