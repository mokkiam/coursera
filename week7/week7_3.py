numbers = [int(s) for s in input().split()]
occurance = set()
for num in numbers:
    if num in occurance:
        print('YES')
    else:
        print('NO')
        occurance.add(num)
