
# Дано натуральное число. Найдите цифру, стоящую в разряде десятков в его десятичной записи (вторую справа цифру или 0, если число меньше 10).
#
# Замечание
#
# Предполагается решение этой задачи без использования строковых методов. Пожалуйста, пользуйтесь арифметикой.
N = int(input())
print(N // 10 % 10)
