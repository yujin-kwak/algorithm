T = int(input())
for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    res = 0

    if a == b:
        res = c
    elif a == c:
        res = b
    else:
        res = a

    print("#{} {}".format(test_case, res))