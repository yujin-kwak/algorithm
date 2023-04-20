board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    for j in range(3):
        tmp = board[i][j:j+5] #행 확인 (슬라이스 이용)
        for k in range(2):
            if tmp[k] != tmp[-1-k]:
                break
        else:
            cnt += 1

        # 열 확인 (슬라이스 사용 못함)
        for k in range(2):
            if board[j + k][i] != board[j+5-k-1][i]:
                break
        else:
            cnt += 1

print(cnt)
