import sys

testNum = int(input())

for _ in range(testNum):
    n = int(input())
    rank = []

    for i in range(n):
        rank.append(list(map(int, sys.stdin.readline().split())))

    rank.sort(key=lambda x: x[0])
    cnt = 1
    man = rank[0][1]
    for i in range(1, n):
        if rank[i][1] < man:
            man = rank[i][1]
            cnt += 1

    print(cnt)