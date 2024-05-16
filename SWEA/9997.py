T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    res = int(n * 2)
    if res / 60 == 0:
        h = 0
        m = res
    else:
        h = int(res / 60)
        m = int(res % 60)

    print("#{} {} {}".format(test_case, h, m))