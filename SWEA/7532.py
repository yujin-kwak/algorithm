T = int(input())
for test_case in range(1, T + 1):
    S, E, M = map(int, input().split())
    res = 1

    while(True):
        if (res - S) % 365 == 0 and (res - E) % 24 == 0 and (res - M) % 29 == 0:
            break
        else:
            res += 1

    print(res)