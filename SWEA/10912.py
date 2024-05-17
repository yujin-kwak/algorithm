T = int(input())
for test_case in range(1, T + 1):
    in_str = list(input())
    eng = [0] * 26

    for i in range(len(in_str)):
        if eng[ord(in_str[i]) - 97] == 0:
            eng[ord(in_str[i]) - 97] = 1
        else:
            eng[ord(in_str[i]) - 97] = 0

    res = ''
    if sum(eng) == 0:
        res = 'Good'
    else:
        for i in range(26):
            if eng[i] == 1:
                res += chr(i + 97)

    print("#{} {}".format(test_case, res))