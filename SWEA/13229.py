T = int(input())
for test_case in range(1, T + 1):
    arr = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    in_str = input()
    res = 0

    for i in range(7):
        if in_str == arr[i]:
            res = 6 - i

            if res == 0:
                res = 7

    print("#{} {}".format(test_case, res))