
#Дано трехзначное число. Найдите сумму его цифр.
N = int(input())
first = N % 10
tens = N // 10 % 10
hundreds = N // 100
summ = first + tens + hundreds
print(summ)
