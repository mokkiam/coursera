a, b, c = int(input()), int(input()), int(input())
if b < a:
    (a, b) = (b, a)
if c < b:
    (b, c) = (c, b)
if c < a:
    (a, c) = (c, a)
if b < a:
    (a, b) = (b, a)
print(a, b, c)
