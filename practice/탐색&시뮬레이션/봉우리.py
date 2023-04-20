n = int(input()) # 격자 크기 n * n
board = [list(map(int, input().split())) for _ in range(n)] # 격자 받아오기

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cnt = 0
for i in range(n):
    for j in range(n):
        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]
            if 0 <= ny < n and 0 <= nx < n :
                if board[i][j] > board[ny][nx]:
                    continue
                else:
                    break
        else:
            cnt += 1

print(cnt)