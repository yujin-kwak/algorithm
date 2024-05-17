T = int(input())
for test_case in range(1, T + 1):
    m, d = map(int, input().split())
    for i in range(m - 1, 0, -1):
        if i == 1:
            d += 31
        elif i == 2:
            d += 29
        elif i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            d += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            d += 30

    res = d % 7 + 3
    if res >= 7:
        res -= 7

    print("#{} {}".format(test_case, res))