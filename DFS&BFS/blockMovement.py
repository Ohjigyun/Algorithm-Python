from collections import deque

def get_next_pos(pos, board):
    #이동 가능한 위치
    next_pos = []
    #현재 위치 정보를 리스트로 변환
    pos = list(pos)
    pos1_x , pos1_y , pos2_x , pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1 , 1 , 0 , 0]
    dy = [0 , 0 , -1 , 1]
    for i in range(4):
        pos1_next_x , pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i] , pos1_y + dy[i] , pos2_x + dx[i] , pos2_y + dy[i]
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x , pos2_next_y )})
    if pos1_x == pos2_x:
        for i in [-1 , 1]: 
            if board[pos1_x + i ][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i , pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    elif pos1_y == pos2_y:
        for i in [-1 , 1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i ] ==0:
                next_pos.append({(pos1_x , pos1_y), (pos1_x , pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    #현재 위치에서 이동할 수 있는 위치를 리턴
    return next_pos

def solution(board):
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    q = deque()
    visited = []
    pos = {(1,1), (1,2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos , cost = q.popleft()
        if (n,n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)
    return 0
    
# 프로그래머스 자바스크립트 답안(양대환님)
# // 따라함 : https://jennylee4517.github.io/ps/2020%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%B5%EC%B1%84-5/ 

# function solution(map) {
#     const n = map.length,
#       dx = [0, 0, 1, -1],
#       dy = [1, -1, 0, 0],
#       rowToColDx = [-1, -1, 0, 0],
#       rowToColDy = [0, 1, 0, 1],
#       colToRowDx = [0, 1, 0, 1],
#       colToRowDy = [0, 0, -1, -1],
#       q = [
#         [0, 0, 0, 0]
#       ],
#       visited = [];

#     for (let i = 0; i < n; i++) {
#       visited.push([]);
#       for (let j = 0; j < n; j++) {
#         visited[i].push([Infinity, Infinity]);
#       }
#     }

#     visited[0][0][0] = 0;

#     let min = Infinity;

#     const canGoRight = (x, y, p) => {
#       if(p === 0) {
#         if(y+2 >= n || map[x][y+1] === 1 || map[x][y+2] === 1)
#           return false;
#       }else {
#         if(y+1 >= n || x+1 >= n || map[x][y+1] === 1 || map[x+1][y+1] === 1)
#           return false;
#       }
#       return true;
#     };

#     const canGoLeft = (x, y, p) => {
#       if(p === 0) {
#         if(y-1 < 0 || map[x][y-1] === 1)
#           return false;
#       }else {
#         if(y-1 < 0 || x+1 >= n || map[x][y-1] === 1 || map[x+1][y-1] === 1)
#           return false;
#       }
#       return true;
#     };

#     const canGoDown = (x, y, p) => {
#       if(p === 0) {
#         if(x+1 >= n || y+1 >= n || map[x+1][y] === 1 || map[x+1][y+1] === 1)
#           return false;
#       }else {
#         if(x+2 >= n || map[x+1][y] === 1 || map[x+2][y] === 1) {
#           return false;
#         }
#       }
#       return true;
#     };

#     const canGoUp = (x, y, p) => {
#       if(p === 0) {
#         if(x-1 < 0 || y+1 >= n || map[x-1][y] === 1 || map[x-1][y+1] === 1)
#           return false;
#       }else {
#         if(x-1 < 0 || map[x-1][y] === 1) {
#           return false;
#         }
#       }
#       return true;
#     };

#     const canRotateUp = (x, y) =>
#       !(x - 1 < 0 || y + 1 >= n || map[x - 1][y] === 1 || map[x - 1][y + 1] === 1);

#     const canRotateDown = (x, y) =>
#       !(x + 1 >= n || y + 1 >= n || map[x + 1][y] === 1 || map[x + 1][y + 1] === 1);

#     const canRotateRight = (x, y) =>
#       !(y + 1 >= n || x + 1 >= n || map[x][y + 1] === 1 || map[x + 1][y + 1] === 1);

#     const canRotateLeft = (x, y) =>
#       !(y - 1 < 0 || x + 1 >= n || map[x][y - 1] === 1 || map[x + 1][y - 1] === 1);

#     const canGoMap = [
#       canGoRight,
#       canGoLeft,
#       canGoDown,
#       canGoUp
#     ],
#       canRotateMap = [
#         [
#           canRotateUp,
#           canRotateUp,
#           canRotateDown,
#           canRotateDown
#         ], [
#           canRotateRight,
#           canRotateRight,
#           canRotateLeft,
#           canRotateLeft
#         ],
#       ],

#       deltaMap = [
#         [rowToColDx, rowToColDy],
#         [colToRowDx, colToRowDy]
#       ];

#     while (q.length) {
#       const [x, y, t, p] = q.shift();

#       // 만일 (n,n)에 도착했다면 최소시간을 갱신합니다
#       if (
#         (x === n - 1 && y === n - 2 && p === 0)
#         || (x === n - 2 && y === n - 1 && p === 1)
#       ) {
#         min = Math.min(min, t);
#       }

#       // 회전 없이 우좌하상으로 움직일때
#       for (let k = 0; k < 4; k++) {
#         if (!canGoMap[k](x, y, p)) {
#           continue;
#         }

#         const nx = x + dx[k],
#           ny = y + dy[k];

#         if (visited[nx][ny][p] > t + 1) {
#           visited[nx][ny][p] = t + 1;
#           q.push([nx, ny, t + 1, p]);
#         }
#       }

#       for (let k = 0; k < 4; k++) {
#         // 가로로 놓인 상황인 경우 세로로 돌려보자
#         // 세로로 놓인 상황인 경우 가로로 돌려보자

#         if (!canRotateMap[p][k](x, y)) continue;

#         const nx = x + deltaMap[p][0][k],
#           ny = y + deltaMap[p][1][k],
#           _p = p ? 0 : 1;

#         if (visited[nx][ny][_p] > t + 1) {
#           visited[nx][ny][_p] = t + 1;
#           q.push([nx, ny, t + 1, _p]);
#         }
#       }

#     }

#     return min;
#   }

    
    
    