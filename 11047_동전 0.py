n, k = map(int, input().split())
unit = []
answer = 0

for _ in range(n):
  unit.append(int(input()))

unit.sort(reverse=True)

for i in unit:
  answer += k // i
  k %= i

print(answer)