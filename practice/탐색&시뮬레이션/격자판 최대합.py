n = int(input())
board = [list(map(int, input().split())) for _ in range(n)] # 격자판 읽기
max_sum = 0

# 행과 열의 최대합 구하기
for i in range(n):
    row_sum = 0
    col_sum = 0
    for j in range(n):
        row_sum += board[i][j]
        col_sum += board[j][i]
    if max_sum < row_sum:
        max_sum = row_sum
    if max_sum < col_sum:
        max_sum = col_sum

# 두개의 대각선의 최대합 구하기
dia_sum1 = 0
dia_sum2 = 0
for i in range(n):
    dia_sum1 += board[i][i]
    dia_sum2 += board[i][n-i-1]

if max_sum < dia_sum1:
    max_sum = dia_sum1
if max_sum < dia_sum2:
    max_sum = dia_sum2

print(max_sum)