T = int(input())
for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())
    min_bread = min(A, B)
    res = int(C / min_bread)
    print("#{} {}".format(test_case, res))