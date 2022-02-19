# 특정한 노드에서 다른 모든 노드로 가는 최단 경로를 계산.
# 음의 간선이 없을 때만 정상적으로 동작한다.
# 매 상황에서 가장 비용이 적은 노드를 선택해 과정을 반복

# 알고리즘의 동작 원리는 아래와 같다.
# 1. 출발 노드를 설정한다.
# 2. 최단 거리 테이블을 초기화한다.
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산해 최단 거리 테이블을 갱신한다.
# 5. 위 과정에서 3번과 4번을 반복한다.

import sys
input = sys.stdin.readline
INF = int(1e9)
# 노드의 수 , 간선의 수 
n , m = map(int , input().split())
# 시작 노드 번호 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
#방문한 적이 있는지를 확인하는 리스트 만들기
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a , b , c = map(int , input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i 
    return index

def dijkstra(start):
    #시작 노드에 대해 초기화
    distance[start] = 0 
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)
#distance 리스트가 모든 노드에 대한 최단 거리 정보를 가짐

