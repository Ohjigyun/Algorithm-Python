from collections import deque

n , l , r = map(int , input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int , input().split())))

dx = [-1 , 0, 1, 0]
dy = [0 , -1 , 0 , 1]
result = 0

#특정 위치에서 출발해 모든 연합을 체크 후 데이터를 갱신
def process(x, y , index):
    #(x, y)의 위치에 연결된 나라 정보를 담는 리스트
    united = []
    united.append((x,y))
    # BFS 큐 자료구조 정의
    q = deque()
    q.append((x,y))
    
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny and union[nx][ny] == -1:
                #옆에 있는 나라와 인구 차이가 L 이상 R이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx,ny))
    for i , j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j,index)
                index+= 1
            if index == n*n :
                break
            total_count += 1
#인구 이동 횟수 출력
print(total_count)