print(*list(map(lambda c: (c[0] + c[1]) % 2, zip(map(int, input().split()), map(int, input().split())))))
