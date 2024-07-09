import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N and 0 <= ny < M):
            if board[nx][ny] == 1:
                board[nx][ny] -= 1
                dfs(nx, ny)

for test_case in range(T):
    M, N, K = map(int, input().strip().split())
    board = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        y, x = map(int, input().split())
        board[x][y] = 1

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                dfs(i, j)
                count += 1

    print(count)