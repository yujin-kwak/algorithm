dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x, d):
    global temp
    if d == 6:
        res.append(temp)
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            temp += str(board[ny][nx])
            dfs(ny, nx, d + 1)
            temp = temp[:-1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    res=[]

    for y in range(4):
        for x in range(4):
            temp = str(board[y][x])
            dfs(y, x, 0)

    ans = set(res)
    print('#{0} {1}'.format(test_case, len(ans)))

