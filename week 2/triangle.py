a, b, c = int(input()), int(input()), int(input())
if b < a:
    (a, b) = (b, a)
if c < b:
    (b, c) = (c, b)
if c < a:
    (a, c) = (c, a)
if b < a:
    (a, b) = (b, a)
if a + b <= c or a + c <= b or b + c <= a:
    print("impossible")
elif a**2 + b**2 == c**2:
    print("rectangular")
elif a**2 + b**2 > c**2:
    print("acute")
elif a ** 2 + b ** 2 < c ** 2:
    print("obtuse")
