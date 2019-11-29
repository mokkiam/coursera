def power(a, n):
    if a == 0:
        return 0
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return power(a, n/2) ** 2
    else:
        return a * power(a, n-1)


a1 = float(input())
n1 = int(input())

print(power(a1, n1))
