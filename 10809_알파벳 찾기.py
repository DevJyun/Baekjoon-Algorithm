str = input()
alpha = [-1]*26

for i in range(len(str)):
    index = ord(str[i]) - 97
    if alpha[index] == -1:
        alpha[index] = i

for i in alpha:
    print(i, end=' ')