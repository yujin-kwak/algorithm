T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    res = N
    for i in range(N):
        if i == 0:
            res += arr[i] * 2
        else:
            res += arr[i]

    print("#{} {}".format(test_case, res))
