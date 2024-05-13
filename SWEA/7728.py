T = int(input())

for test_case in range(1, T + 1):
    in_str = list(input())
    arr = [0] * 10
    for i in range(len(in_str)):
        arr[int(in_str[i])] = 1

    print("#{} {}".format(test_case, sum(arr)))