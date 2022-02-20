# 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용한다.
# 사이클 판별 알고리즘은 다음과 같다.
# 1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인한다.
#     i) 루트 노드가 서로 다르다면 두 노드에 대해 합집합 연산을 수행한다.
#     ii) 루트 노드가 서로 같다면 사이클이 발생한 것
# 2. 그래프에 포함되어 있는 모든 간선에 대해 1번 과정을 반복한다.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int , input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int , input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)
    