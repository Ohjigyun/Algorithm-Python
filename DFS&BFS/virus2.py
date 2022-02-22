from collections import deque

n , k = map(int, input().split())

#보드 정보를 담는 리스트
graph = []
#바이러스 정보를 담는 리스트
data = []

for i in range(n):
    #보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        #해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # 바이러스 종류 , 시간 , 위치 X , 위치 Y
            data.append((graph[i][j], 0, i, j))

#낮은 숫자가 먼저 증식하므로
data.sort()
q = deque(data)

target_s , target_x , target_y = map(int , input().split())

dx = [-1 , 0 , 1, 0]
dy = [0 , 1 , 0 , -1]

while q:
    virus , s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1 , nx, ny))

print(graph[target_x - 1][target_y - 1])