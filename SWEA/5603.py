T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    S = []
    for i in range(N):
        S.append(int(input()))

    avg = sum(S) / N

    sum_v = 0
    for i in range(N):
        if S[i] < avg:
            sum_v += int(avg) - S[i]

    print("#{} {}".format(test_case, sum_v))