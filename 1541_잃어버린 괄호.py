a = input().split('-')
arr = []
answer = 0

for i in a:
    s = i.split('+')
    sum = 0

    for j in s:
        sum += int(j)

    arr.append(sum)

answer += arr[0]
for i in range(1, len(arr)):
    answer -= arr[i]

print(answer)