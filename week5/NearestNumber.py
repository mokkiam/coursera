N = int(input())
s = input()
a = [int(s) for s in s.split()]
x = int(input())
b = [abs(a[i]-x) for i in range(len(a))]
print(a[b.index(min(b))])
