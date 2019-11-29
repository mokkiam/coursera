import math


def MinDivisor(n):
    d = 2
    while n % d != 0 and d < math.sqrt(n):
        d += 1
    if d > math.sqrt(n):
        return n
    else:
        return d


n1 = int(input())
print(MinDivisor(n1))
