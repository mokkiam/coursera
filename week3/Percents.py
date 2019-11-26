p = int(input())
x = int(input())
y = int(input())

res = x*100+y + (x*100+y)*(p/100)
print(int(res/100), int(res % 100))
