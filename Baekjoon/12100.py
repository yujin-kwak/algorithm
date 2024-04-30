import copy

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def left(board):
    for i in range(N):
        cursor = 0
        for j in range(1, N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
                
                if board[i][cursor] == 0:
                    board[i][cursor] = tmp

                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor += 1
                
                else:
                    cursor += 1
                    board[i][cursor] = tmp 
    return board

def right(board):
    for i in range(N):
        cursor = N - 1
        for j in range(N - 2, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                
                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor -= 1
                
                else:
                    cursor -= 1
                    board[i][cursor] = tmp
    return board

def up(board):
    for i in range(N):
        cursor = 0
        for j in range(1, N):
            if board[j][i] != 0:
                tmp = board[j][i]
                board[j][i] = 0

                if board[cursor][i] == 0:
                    board[cursor][i] = tmp
                
                elif board[cursor][i] == tmp:
                    board[cursor][i] *= 2
                    cursor += 1
                
                else:
                    cursor += 1
                    board[cursor][i] = tmp
    return board

def down(board):
    for i in range(N):
        cursor = N - 1
        for j in range(N - 2, -1, -1):
            if board[j][i] != 0:
                tmp = board[j][i]
                board[j][i] = 0

                if board[cursor][i] == 0:
                    board[cursor][i] = tmp
                
                elif board[cursor][i] == tmp:
                    board[cursor][i] *= 2
                    cursor -= 1
                
                else:
                    cursor -= 1
                    board[cursor][i] = tmp
    return board

def dfs(n, arr):
    global ans
    if n == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return
    
    for i in range(4):
        copy_arr = copy.deepcopy(arr)
        if i == 0:
            dfs(n + 1, left(copy_arr))
        elif i == 1:
            dfs(n + 1, right(copy_arr))
        elif i == 2:
            dfs(n + 1, up(copy_arr))
        else:
            dfs(n + 1, down(copy_arr))

dfs(0, map)
print(ans)
