a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

delta = a * d - b * c
delta1 = e * d - f * b
delta2 = a * f - c * e
print(float(delta1/delta), float(delta2/delta))
