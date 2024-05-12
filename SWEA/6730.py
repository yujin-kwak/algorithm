T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = list(map(int,input().split()))
    print('arr', arr)
    max_v = 0
    min_v = 0
    for i in range(N - 1):
        if arr[i] <= arr[i+1]:
            val = arr[i+1] - arr[i]
            max_v = max(val, max_v)
        else:
            val = arr[i] - arr[i+1]
            min_v = max(val, min_v)
    
    print("#{} {} {}".format(test_case, max_v, min_v))

