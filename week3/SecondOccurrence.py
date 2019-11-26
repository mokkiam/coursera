stroka = input()
f = 0

for i in stroka:
    if i == "f":
        f += 1

if f == 1:
    print(-1)
elif f == 0:
    print(-2)
else:
    print(stroka.find('f', stroka.find('f')+1))
