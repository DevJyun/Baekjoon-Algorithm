n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

answer = cost[0] * dist[0]
now = cost[0]

for i in range(1, n - 1):
    if now > cost[i]:
        now = cost[i]

    answer += (now * dist[i])

print(answer)