from itertools import combinations

n = int(input())
board = []
teachers = []
space = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j))
        if board[i][j] == 'X':
            space.append((i,j))

#특정 방향에 존재하는 학생에 대한 감시를 진행
def watch(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False
#장애물 설치 이후의 학생 감지 결과를 검사
def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False

#빈 공간에서 3개를 뽑는 모든 조합을 확인

for data in combinations(space, 3):
    for x ,y in data:
        board[x][y] = 'O'
    if not process:
        find = True
        break
    for x, y, in data:
        board[x][y] = 'X'

if find:
    print('Yes')
else:
    print('No')