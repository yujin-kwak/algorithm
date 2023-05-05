from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

m , n = map(int, input().split()) # m: 가로칸 수, n: 세로 칸 수
board = [list(map(int, input().split())) for _ in range(n)]
qu = deque([])
res = 0

# queue에 처음에 받은 토마토의 위치 좌표를 append 함
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            qu.append([i, j])

def bfs():
    while qu:
        y, x = qu.popleft()
        # 상하좌우 확인
        for w in range(4):
            ny = y + dy[w]
            nx = x + dx[w]
            # 좌표가 좌표 크기를 넘어가지 않고, 그 좌표의 토마토가 익지 않은 상태여야함(0).
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0:
                board[ny][nx] = board[y][x] + 1
                qu.append([ny, nx])

bfs()

for i in board:
    for j in i:
        # 확인했을 때 모든 토마토를 익히지 못했다면 -1
        if j == 0:
            print(-1)
            exit(0)
    # 모든 토마토를 익혔다면 최댓값
    res = max(res, max(i))
# 처음에 1부터 시작했으므로 1을 뺌
print(res - 1)
