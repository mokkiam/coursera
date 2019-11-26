import math


def IsPrime(n):
    i = 2

    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    else:
        return True


n1 = int(input())

if IsPrime(n1):
    print("YES")
else:
    print("NO")
