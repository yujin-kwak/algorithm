T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    K = int(N/2)
    sum_v = 0
    s = 0
    for i in range(K + 1):
        sum_v += sum(board[i][K-s:K+s+1])
        s += 1

    s -= 2
    for i in range(K + 1, 2 * K + 1):
        sum_v += sum(board[i][K-s:K+s+1])
        s -= 1

    print("#{} {}".format(test_case, sum_v))