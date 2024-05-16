T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    M = list(input().split())
    M.sort(reverse=True)
    select = M[0:K]
    re_select = select[::-1]
    A = 0

    for i in range(K):
        res = (A + int(re_select[i])) / 2
        A = res

    print("#{} {}".format(test_case, format(A, ".6f")))