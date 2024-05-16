T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(input().split())

    if N % 2 == 0:
        k = int(N / 2)
    else:
        k = int(N / 2) + 1

    str1 = arr[0:k]
    str2 = arr[k:N]

    res = []
    for i in range(k):
        res.append(str1[i])
        if i < len(str2):
            res.append(str2[i])

    print("#{}".format(test_case), *res)