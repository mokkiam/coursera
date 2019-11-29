stroka = input()
start = stroka.find('h')
end = stroka.rindex('h')

print(stroka[0:start], stroka[end+1:stroka.__len__()], sep='')
