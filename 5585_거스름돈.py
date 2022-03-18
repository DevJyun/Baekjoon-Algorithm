pay = int(input())
change = 1000 - pay
unit = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in unit:
  cnt += change // i
  change %= i

print(cnt)