stroka = input()
f = 0

for i in stroka:
    if i == "f":
        f += 1

if f == 1:
    print(stroka.find('f'))
elif f > 1:
    print(stroka.find('f'), stroka.rindex('f'))
