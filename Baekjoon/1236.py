import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().strip()) for _ in range(N)]

res1 = 0
for i in range(N):
    cnt = 0
    for j in range(M):
        if board[i][j] == '.':
            cnt += 1
        else:
            break
    if cnt == M:
        res1 += 1

res2 = 0
for i in range(M):
    cnt = 0
    for j in range(N):
        if board[j][i] == '.':
            cnt += 1
        else:
            break
    if cnt == N:
        res2 += 1

print(max(res1, res2))