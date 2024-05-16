T = int(input())
for test_case in range(1, T + 1):
    in_str = input().split()
    res = in_str[0][0].upper() + in_str[1][0].upper() + in_str[2][0].upper()
    print("#{} {}".format(test_case, res))