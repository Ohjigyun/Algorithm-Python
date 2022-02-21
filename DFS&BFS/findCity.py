# 어떤 나라엔 1~ N번 까지의 도시와 M개의 단방향 도로가 존재합니다.
# 모든 도로의 거리는 1이며 특성한 도시 X로부터 출발하여 도달할 수 있는
# 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램을 작성하세요.

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a , b = map(int, input().split())
    graph[a].append(b)
# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 

q = deque([x])
while q:
    now = q.popleft()
#현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            
check=False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
        
if check == False:
    print(-1)