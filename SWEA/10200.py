T = int(input())
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    min_v = (A + B) - N
    max_v = min(A, B)

    if min_v < 0:
        min_v = 0

    print("#{} {} {}".format(test_case, max_v, min_v))