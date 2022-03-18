t = int(input())
seconds = [300, 60, 10]
answer = [0, 0, 0]

for i in range(len(seconds)):
  if t >= seconds[i]:
    answer[i] = t//seconds[i]
    t %= seconds[i]

    if t <= 0:
      break

if t != 0:
  print('-1')
else:
  for i in answer:
    print(i, end=' ')