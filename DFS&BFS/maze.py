# 동빈이는 n X m 크기의 직사각형 형태의 미로에 갇혔습니다.
# 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
# 동빈이의 위치는 (1,1)이며 미로의 출구는 (n,m)의 위치에 존재하며
# 한 번에 한 칸씩 이동할 수 있습니다.
# 이 때, 괴물이 있는 부분은 0으로 괴물이 없는 부분은 1로 표시되어 있습니다.
# 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
# 이 때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요.

#BFS를 이용한 풀이)
from collections import deque

n , m = map(int , input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0 , 0]
dy = [0 , 0 , -1 , 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x , y = queue.popleft()
        #현재 위치에서 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #공간을 벗어나면 무시
            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue
            # 벽이면 무시
            if graph[nx][ny] ==0:
                continue
            #해당 노드를 처음 방문하면 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
    return graph[n-1][m-1]