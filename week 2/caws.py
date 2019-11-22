n = int(input())
if 11 < n < 14 or n % 10 in (0, 5, 6, 7, 8, 9):
    print(n, "korov")
elif n % 10 == 1:
    print(n, "korova")
else:
    print(n, "korovy")
