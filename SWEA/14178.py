T = int(input())
for test_case in range(1, T + 1):
    N, D = map(int, input().split())
    res = int(N / (D * 2 + 1))

    if N % (D * 2 + 1) != 0:
        res += 1

    print("#{} {}".format(test_case, res))