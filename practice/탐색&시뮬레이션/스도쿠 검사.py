def check(board):
    # 행과 열 검사
    for i in range(9):
        ch_row = [0] * 10 # 행 체크 리스트
        ch_col = [0] * 10 # 열 체크 리스트
        for j in range(9):
            ch_row[board[i][j]] = 1
            ch_col[board[i][j]] = 1
        if sum(ch_row) != 9 or sum(ch_col) != 9: # 체크 리스트 합이 9가 아니면 잘못 푼 스도쿠
            return False

    # 그룹 검사 3*3
    for i in range(3):
        for j in range(3): # i와 j로 9개의 그룹을 정함
            ch_g = [0] * 10 # 그룹 정해졌으니 체크 리스트 초기화
            for k in range(3): # 그룹 내 검사
                for s in range(3):
                    ch_g[board[i*3+k][j*3+s]] = 1
            if sum(ch_g) != 9:
                return False
    return True

board = [list(map(int, input().split())) for _ in range(9)]
if check(board): # True를 반환하면 맞는 스도쿠
    print("YES")
else: # False를 반환하면 잘못 푼 스도쿠
    print("NO")