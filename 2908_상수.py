s1, s2 = map(str, input().split())
n1 = int(s1[::-1])
n2 = int(s2[::-1])

if n1 > n2:
    print(n1)
else:
    print(n2)