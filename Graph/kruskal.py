#신장 트리
#그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

#최소 신장 트리 알고리즘(kruskal)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a ,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * ( v + 1)

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0 

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b , cost = map(int , input().split())
    #정렬을 위해 cost 를 맨앞으로
    edges.append((cost, a, b))
#cost 순으로 간선을 정렬
edges.sort()

for edge in edges:
    cost , a , b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
