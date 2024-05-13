T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 문자열 개수
    que_arr = list(input())
    ans_arr = list(input())

    res = 0
    for i in range(N):
        if que_arr[i] == ans_arr[i]:
            res += 1

    print("#{} {}".format(test_case, res))
