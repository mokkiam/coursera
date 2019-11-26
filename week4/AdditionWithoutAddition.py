def sum(a, b):
    if b != 0:
        a = a + 1
        return sum(a, b - 1)
    else:
        return a


a1 = int(input())
b1 = int(input())

print(sum(a1, b1))
