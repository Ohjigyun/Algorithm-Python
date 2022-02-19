# 어떤 나라엔 N개의 도시가 있다. 각 도시에 보내고자 하는 메시지가 있는 경우
# 다른 도시로 전보를 보내 다른 도시로 메시지를 전송할 수 있다.
# 하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로
# 향하는 통로가 설치되어 있어야 한다. 예를 들어 X에서 Y로 향하는 통로는 있지만,
# Y에서 X로 향하는 통로가 없다면 Y는 X로 메시지를 보낼 수 없다.
# 또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.
# 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때 도시 C에서 보낸 메시지를
# 받게되는 도시의 개수는 총 몇개이며 모두 메시지를 받게 될때까지 걸리는 시간을 계산하는
# 프로그램을 작성하세요.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n , m , start = map(int , input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int , input().split())
    graph[x].append((y,z))


def dijkstra(start):
    q = []
    heapq.heappush(q , (0,start))
    distance[start] = 0
    while q:
        dist , now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1 , max_distance)