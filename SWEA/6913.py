T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    sum_v = []

    for i in range(N):
        arr = list(map(int, input().split()))
        sum_v.append(sum(arr))

    max_v = max(sum_v)
    count = 0
    for i in range(N):
        if sum_v[i] == max_v:
            count += 1

    print("#{} {} {}".format(test_case, count, max_v))