from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]

for test_case in range(1, 11):
    T = int(input())
    board = [list(input()) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    q = deque()

    for i in range(100):
        for j in range(100):
            if board[i][j] == '2':
                sx = i
                sy = j
                q.append((sx, sy))
                visited[i][j] = 1

    res = 0
    while q:
        x, y = q.popleft()
        if board[x][y] == '3':
            res = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 99 and 0 <= ny <= 99:
                if board[nx][ny] != '1' and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    print("#{} {}".format(T, res))