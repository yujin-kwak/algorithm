T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    twin = N - M
    uni = M - twin
    print("#{} {} {}".format(test_case, uni, twin))