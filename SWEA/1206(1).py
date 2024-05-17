for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    res = 0
    for i in range(2, N - 2):
        if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            max_v = max(arr[i-1], arr[i-2], arr[i+1], arr[i+2])
            res += arr[i] - max_v

    print("#{} {}".format(test_case, res))