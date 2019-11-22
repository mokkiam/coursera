# Даны три целых числа. Найдите наибольшее из них
# (программа должна вывести ровно одно целое число).
A = int(input())
B = int(input())
C = int(input())
big = A
if B > big:
    big = B
if C > big:
    big = C
print(big)
