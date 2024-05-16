T = int(input())
for test_case in range(1, T + 1):
    eng = [0] * 26
    in_str = list(input())

    for i in in_str:
        eng[ord(i) - 65] += 1

    res = 'Yes'
    for i in range(26):
        if not (eng[i] == 0 or eng[i] == 2):
            res = 'No'

    print("#{} {}".format(test_case, res))