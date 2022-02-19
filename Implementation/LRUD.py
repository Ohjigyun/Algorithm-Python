# 여행가 A는 N X N 크기의 정사각형 공간 위에 서있습니다. 
# 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있고,
# 가장 왼쪽 위 좌표는 (1,1) , 가장 오른쪽 아래는 (N,N)입니다.
# A는 상하좌우로 움직일 수 있으며 시작좌표는 항상 (1,1)입니다.
# 여행가 A의 계획이 담긴 계획서에는 L, R, U, D가 반복적으로 적혀있고
# 각 문자의 의미는 왼쪽 , 오른쪽 , 위로 , 아래로 한칸 이동입니다. 
# 최종 도착할 지점의 좌표를 구하는 프로그램을 작성하세요.

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x,y)