T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    sum_v = [0] * 41

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            sum_v[i + j] += 1

    max_v = 0
    for i in range(len(sum_v)):
        max_v = max(max_v, sum_v[i])

    res = []
    for i in range(len(sum_v)):
        if max_v == sum_v[i]:
            res.append(i)

    print("#{}".format(test_case), *res)
