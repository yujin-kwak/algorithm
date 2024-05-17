T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    pi = list(map(int, input().split()))
    count = 0

    for i in range(1, N - 1):
        arr = pi[i-1:i+2]
        max_v = max(arr)
        min_v = min(arr)
        if pi[i] != max_v and pi[i] != min_v:
            count += 1

    print("#{} {}".format(test_case, count))