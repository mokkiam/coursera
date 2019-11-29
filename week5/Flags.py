N = int(input())
firstLine = ""
secondLine = ""
thirdLine = ""
fourthLine = ""

for i in range(1, N + 1, 1):
    firstLine += '+___ '
    secondLine += '|' + str(i) + ' / '
    thirdLine += '|__\\ '
    fourthLine += '|    '

print(firstLine)
print(secondLine)
print(thirdLine)
print(fourthLine)
