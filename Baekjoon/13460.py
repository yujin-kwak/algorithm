from collections import deque

N, M = map(int, input().split())

board = []

dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

def move(x, y, dx, dy):
    cnt = 0 
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt 

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited = []
    visited.append((rx, ry, bx, by))

    while q:
        rx, ry, bx, by , depth = q.popleft()
            
        if depth > 10:
                return -1
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            
            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    return depth
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt :
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    visited.append((nrx, nry, nbx, nby))
                    q.append((nrx, nry, nbx, nby, depth + 1))
    return -1
res = bfs(rx, ry, bx, by)
print(res)           



