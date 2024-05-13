T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())

    res = 0
    for i in range(A, B + 1):
        if str(i) == str(i)[::-1]:
            val = i ** 0.5
            if val == int(val):
                if str(int(val)) == str(int(val))[::-1]:
                    res += 1

    print("#{} {}".format(test_case, res))