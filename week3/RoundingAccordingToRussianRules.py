import math

x = float(input())

if x % 1 >= 0.5:
    print(math.ceil(x))
else:
    print(math.floor(x))
