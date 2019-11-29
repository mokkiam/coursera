import math

x = math.modf(float(input()))

print(int(x[1]), round(x[0]*100))
