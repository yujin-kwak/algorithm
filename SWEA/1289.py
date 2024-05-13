T = int(input())

for test_case in range(1, T + 1):
    arr = list(input())
    target = '0'
    count = 0

    for i in range(len(arr)):
        if arr[i] != target:
            count += 1
            target = arr[i]

    print("#{} {}".format(test_case, count))