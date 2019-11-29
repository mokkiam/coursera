def add(x, y):
    if y != 0:
        x += y
        return add(x, int(input()))
    else:
        return x


print(add(0, int(input())))
