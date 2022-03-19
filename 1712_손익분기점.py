base, made, cost = map(int, input().split())

if made >= cost:
    print(-1)
else:
    print(int(base/(cost-made))+1)