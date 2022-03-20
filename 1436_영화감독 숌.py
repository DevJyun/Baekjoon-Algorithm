n = int(input())
number = 666

while True:
    if str(number).find('666') != -1:
        n -= 1
        if n == 0:
            break
    number += 1

print(number)