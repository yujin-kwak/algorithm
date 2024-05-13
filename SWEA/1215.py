for test_case in range(1, 11):
    N = int(input())
    map = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8 - N + 1):
            flag = 1
            for k in range(N // 2):
                if map[i][j + k] != map[i][j + N - 1 - k]:
                    flag = 0
                    break
            if flag == 1:
                cnt += 1

    for i in range(8):
        for j in range(8 - N + 1):
            flag = 1
            for k in range(N // 2):
                if map[j + k][i] != map[j + N - 1 - k][i]:
                    flag = 0
                    break
            if flag == 1:
                cnt += 1

    print("#{} {}".format(test_case, cnt))