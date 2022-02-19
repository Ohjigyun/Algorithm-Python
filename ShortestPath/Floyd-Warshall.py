# 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산합니다.
# 단계별로 거쳐가는 노드를 기준으로 알고리즘을 수행합니다.
# 2차원 테이블에 최단 거리 정보를 저장하며 DP 유형에 속합니다.

INF = int(1e9)

#노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1 , n+1):
    for b in range(1 , n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int , input().split())
    graph[a][b] = c

for k in range(1 , n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF" , end =" ")
        else:
            print(graph[a][b], end =" ")
    print()
