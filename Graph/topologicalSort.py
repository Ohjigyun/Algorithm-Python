# 위상 정렬 알고리즘
# 큐를 이용한 위상 정렬 알고리즘의 동작 과정
# 1. 진입 차수가 0인 모든 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
#     i) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
#     ii) 새롭게 진입 차수가 0이 된 노드를 큐에 넣는다.
# - 위상 정렬은 싸이클이 존재하지 않아야 한다.

from collections import deque

v, e = map(int , input().split())
# 모든 노드에 대한 진입 차수는 0
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    #정점 a에서 b로 이동 가능
    graph[a].append(b) 
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    #진입 차수가 0인 노드를 큐에 삽입  
    for i in range(1, v+1):
        if(indegree[i]) == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            #새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=' ')

topology_sort()
