T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    sum_v = 0
    for i in range(N):
        p, q = input().split()
        sum_v += float(p) * int(q)
    print("#{} {}".format(test_case, format(sum_v, ".6f")))