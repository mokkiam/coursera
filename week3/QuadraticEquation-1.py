import math

a = float(input())
b = float(input())
c = float(input())
d = b**2-4*a*c

if d > 0:
    result = ((-b - math.sqrt(d))/(2*a), (-b + math.sqrt(d))/(2*a))
    print(min(result), max(result))
elif d == 0:
    print(-b/(2*a))
