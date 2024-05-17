T = int(input())
eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for test_case in range(1, T + 1):
    in_str = list(input())
    res = 0
    for i in range(len(in_str)):
        if in_str[i] == eng[i]:
            res += 1
        else:
            break

    print("#{} {}".format(test_case, res))