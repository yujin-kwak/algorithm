T = int(input())
for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    ans = [0] * (N + 1)
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L, R + 1):
            ans[j] = i

    print("#{}".format(test_case), *ans[1:N+1])