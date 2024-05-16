T = int(input())
for test_case in range(1, T + 1):
    in_num = map(int, input())
    num = [0] * 10

    for i in in_num:
        if num[i] == 0:
            num[i] = 1
        else:
            num[i] = 0

    res = sum(num)
    print("#{} {}".format(test_case, res))
