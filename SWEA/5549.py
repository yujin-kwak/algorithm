T = int(input())
for test_case in range(1, T + 1):
    N = list(map(int, input()))
    if N[-1] % 2 == 0:
        res = 'Even'
    else:
        res = 'Odd'
    print("#{} {}".format(test_case, res))