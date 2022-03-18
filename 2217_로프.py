n = int(input())
rope = []
weight = []

for _ in range(n):
  rope.append(int(input()))

rope.sort()

for i in range(n):
  weight.append(rope[i] * (n-i))

print(max(weight))