n = int(input())
answer = 0

for i in range(n):
    num = sum(map(int, str(i)))

    if num+i == n:
        answer = i
        break

print(answer)