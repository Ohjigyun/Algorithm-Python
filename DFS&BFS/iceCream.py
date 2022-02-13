# n X m 크기의 얼음 틀이 있습니다. 구멍이 뚫려있는 부분은 0, 
# 칸막이가 존재하는 부분은 1로 표시됩니다. 구멍이 뚫려있는 부분끼리
# 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어 있는것으로 간주합니다.
# 이 때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를
# 구하는 프로그램을 작성하세요. 

# DFS를 이용한 풀이)
# 1. 특정한 지점의 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서
# 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
# 2. 방문한 지점에서 다시 상, 하, 좌, 우를 살피면서 방문을 진행하는 과정을
# 반복하면, 연결된 모든 지점을 방문할 수 있다.
# 3. 모든 노드에 대해 1~2번을 반복하고 방문하지 않은 지점의 수를 카운트한다.

n , m = map(int, input().split())
graph = []
# dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나면 종료
    if x <=1 or x >= n or y <= -1 or y >= m:
        return False
    #현재 노드를 방문하지 않았다면
    if graph[x][y] ==0:
        graph[x][y] = 1
        #상하좌우에 대해 재귀적 호출
        dfs(x - 1 , y)
        dfs(x, y-1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False
# 2차원 리스트의 맵 정보 입력받기
for i in range(n):
    graph.append(list(map(int,input())))
#모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)

