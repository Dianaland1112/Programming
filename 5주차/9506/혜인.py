while(1):
    sum = 0
    divisors = []
    a = int(input())
    if a == -1:
        break
    for i in range(1, a):
        if a % i == 0:
            sum += i
            divisors.append(i)
    if sum == a:
        print(a, "=", " + ".join(map(str, divisors)))
    else:
         print(a, "is NOT perfect.")