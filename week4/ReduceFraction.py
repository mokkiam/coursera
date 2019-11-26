import math


def ReduceFraction(n, m):
    k = math.gcd(n, m)
    return n // k, m // k


n1 = int(input())
m1 = int(input())

print(*ReduceFraction(n1, m1))
