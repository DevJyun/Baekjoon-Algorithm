n = int(input())
timeArray = []

for _ in range(n):
    a, b = map(int, input().split())
    timeArray.append([a, b])

timeArray.sort(key=lambda x: x[0])
timeArray.sort(key=lambda x: x[1])

cnt = 1
end = timeArray[0][1]

for i in range(1, n):
    if timeArray[i][0] >= end:
        cnt += 1
        end = timeArray[i][1]

print(cnt)
