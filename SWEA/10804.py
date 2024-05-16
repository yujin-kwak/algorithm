T = int(input())
for test_case in range(1, T + 1):
    arr = list(input())
    res = ''

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 'q':
            res += 'p'
        elif arr[i] == 'p':
            res += 'q'
        elif arr[i] == 'b':
            res += 'd'
        elif arr[i] == 'd':
            res += 'b'

    print("#{} {}".format(test_case, res))
