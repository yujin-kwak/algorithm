T = int(input())
for test_case in range(1, T + 1):
    D, H, M = map(int, input().split())
    D -= 11
    H -= 11
    M -= 11

    res = D * 24 * 60 + H * 60 + M
    if res < 0:
        res = -1

    print("#{} {}".format(test_case, res))