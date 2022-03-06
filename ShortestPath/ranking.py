INF = int(1e9)

#노드의 개수, 간ㅓㄴ의 개수 입력 받기
n , m = map(int , input().split())
#2차원 리스트 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1 , n + 1):
    for b in range(1 , n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    #A 에서 B로 가는 비용을 1로 설정
    a , b = map(int , input().splice())
    graph[a][b] = 1

for k in range(1 , n+1):
    for a in range(1 , n+1):
        for b in range(1 , n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] +graph[k][b])

result = 0 
#각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지를 체크
for i in range(1 , n+1):
    count = 0 
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1

print(result)
