from collections import deque
import copy

# 노드의 개수
v = int(input())
# 모든 노드에 대한 진입차수 초기화
indegree = [0] * (v+1)
#각 노드에 연결된 간선 정보를 담기 위해 연결 리스트 초기화
graph = [[] for i in range(v+1)]
#각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
        
# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    
    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i] , result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
                
    for i in range(1, v + 1):
        print(result[i])
        
topology_sort()
