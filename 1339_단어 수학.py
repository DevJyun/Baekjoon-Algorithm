n = int(input())
words = []
alpha = [0]*26
sum = 0
num = 9

for _ in range(n):
  words.append(list(input()))

for word in words:
  for i in range(len(word)):
    index = ord(word[i])-65
    value = pow(10, len(word)-i-1)
    alpha[index] += value

alpha.sort(reverse=True)

for n in alpha:
  sum += n * num
  num -= 1

  if num <= 0:
    break

print(sum)