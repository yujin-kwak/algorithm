T = int(input())
for test_case in range(1, T + 1):
    now_h, now_m, now_s = map(int, input().split(":"))
    promise_h, promise_m, promise_s = map(int, input().split(":"))

    if promise_s - now_s < 0:
        promise_m -= 1
        promise_s += 60
        s = promise_s - now_s
    else:
        s = promise_s - now_s

    if promise_m - now_m < 0:
        promise_h -= 1
        promise_m += 60
        m = promise_m - now_m
    else:
        m = promise_m - now_m

    if promise_h - now_h < 0:
        promise_h += 24
        h = promise_h - now_h
    else:
        h = promise_h - now_h

    print("#{} {}:{}:{}".format(test_case, format(h, "02"), format(m, "02"), format(s, "02")))