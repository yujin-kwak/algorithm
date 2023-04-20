
import copy

n = int(input()) # 격자 크기 n * n
board = [list(map(int, input().split())) for _ in range(n)] # 격자 안의 감 개수
m = int(input()) # 회전 명령의 개수

for i in range(m):
    row, way, cnt = map(int, input().split()) # 행 번호, 방향, 횟수를 받아옴
    tmp_board = copy.deepcopy(board)
    if way == 0: # 왼쪽
        for j in range(n):
            tmp_board[row-1][(j - cnt) % n] = board[row-1][j]
    else: # 오른쪽
        for j in range(n):
            tmp_board[row-1][(j + cnt) % n] = board[row-1][j]
    board = tmp_board

s, e = 0, n - 1
res = 0
for i in range(n):
    for j in range(s, e + 1):
        res += board[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)

'''
n = int(input()) # 격자 크기 n * n
board = [list(map(int, input().split())) for _ in range(n)] # 격자 안의 감 개수
m = int(input()) # 회전 명령의 개수

for i in range(m):
    row, way, cnt = map(int, input().split()) # 행 번호, 방향, 횟수를 받아옴
    if way == 0:
        for _ in range(cnt):
            board[row-1].append(board[row-1].pop(0)) # 맨 앞의 값을 빼고 나머지를 앞으로 당김, 뺀 값을 맨 뒤에 추가
    else:
        for _ in range(cnt):
            board[row-1].insert(0, board[row-1].pop()) # 맨 뒤의 값을 뺴고 앞에 추가

s = 0
e = n - 1
res = 0
for i in range(n):
    for j in range(s, e + 1):
        res += board[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
'''