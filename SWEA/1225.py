for test_case in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))

    j = 1
    while(True):
        if arr[7] <= 0:
            arr[7] = 0
            break
        arr[0] -= j
        temp = arr[0]
        for i in range(7):
            arr[i] = arr[i + 1]
        arr[7] = temp
        j += 1
        if j > 5:
            j = 1

    print("#{}".format(test_case), *arr)