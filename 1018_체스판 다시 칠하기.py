def checkBoard(low, col, color):
    changeCnt = 0

    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if board[low+i][col+j] != color:
                        changeCnt += 1
                else:
                    if board[low+i][col+j] == color:
                        changeCnt += 1
            else:
                if j % 2 == 0:
                    if board[low+i][col+j] == color:
                        changeCnt += 1
                else:
                    if board[low+i][col+j] != color:
                        changeCnt += 1

    return changeCnt

n, m = map(int, input().split())
board = []
answer = n*m

for i in range(n):
    board.append(list(input()))

for i in range(n-8+1):
    for j in range(m-8+1):
        answer = min(checkBoard(i, j, 'W'), answer)
        answer = min(checkBoard(i, j, 'B'), answer)

print(answer)