lst = [int(i) for i in input().split()]
max_, index = lst[0], 0
for i, x in enumerate(lst):
    if x >= max_:
        max_ = x
        index = i
print(max_, index)
