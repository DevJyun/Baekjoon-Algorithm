t = int(input())
answer = []

for i in range(t):
    r, s = map(str, input().split())
    strTemp = ''
    for c in s:
        strTemp += c*int(r)
    answer.append(strTemp)

for str in answer:
    print(str)