from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) # 격자 크기
    board = [list(map(int, input()))for _ in range(N)]
    q = deque()
    q.append((0, 0))

    time = [[99999] * N for _ in range(N)]
    time[0][0] = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                if time[y][x] + board[ny][nx] < time[ny][nx]:
                    time[ny][nx] = time[y][x] + board[ny][nx]
                    q.append((ny, nx))

    print('#{0} {1}'.format(test_case, time[N-1][N-1]))