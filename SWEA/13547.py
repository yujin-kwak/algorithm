T = int(input())
for test_case in range(1, T + 1):
    arr = list(input())
    count = 0
    for i in range(len(arr)):
        if arr[i] == 'x':
            count += 1

    if count >= 8:
        res = 'NO'
    else:
        res = 'YES'

    print("#{} {}".format(test_case, res))