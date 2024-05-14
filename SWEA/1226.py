from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for T in range(1, 11):
    test_case = int(input())
    map = [list(input()) for _ in range(16)] # map 그리기
    visited = [[0] * 16 for _ in range(16)] # 방문 표시 map 그리기
    q = deque()
    res = 0

    # 출발 지점 찾기
    for i in range(16):
        for j in range(16):
            if map[i][j] == '2':
                sx = i
                sy = j
                q.append((sx, sy))
                visited[sx][sy] = 1

    while(q):
        x, y = q.popleft()
        if map[x][y] == '3':
            res = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 15 and 0 <= ny <= 15:
                if map[nx][ny] != '1' and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    print("#{} {}".format(test_case, res))