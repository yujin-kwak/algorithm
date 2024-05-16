T = int(input())
number = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    find_arr = []

    for i in range(N):
        for j in range(M - 1, -1, -1):
            if board[i][j] == '1':
                find_arr = board[i][j-55:j+1]
                break

    res = []
    for i in range(8):
        arr = find_arr[i*7:(i+1)*7]
        for j in range(10):
            if ''.join(arr) == number[j]:
                res.append(j)

    sum_even = 0
    sum_odd = 0
    for i in range(8):
        if i % 2 == 0: # 홀수자리
            sum_odd += res[i]
        else: # 짝수자리 수
            sum_even += res[i]

    if (sum_odd * 3 + sum_even) % 10 == 0:
        ans = sum_odd + sum_even
    else:
        ans = 0

    print("#{} {}".format(test_case, ans))