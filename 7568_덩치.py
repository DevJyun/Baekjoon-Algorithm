person = int(input())
student = []
answer = []

for _ in range(person):
    student.append(list(map(int, input().split())))

for i in student:
    cnt = 0
    for j in student:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    answer.append(cnt+1)

for i in answer:
    print(i, end=' ')