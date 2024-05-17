T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []

    for i in range(1, N + 1):
        arr.append(i)

    count = 0
    for i in range(N):
        for j in range(i, N + 1):
            if sum(arr[i:j]) == N:
                count += 1
            if sum(arr[i:j]) > N:
                break

    print("#{} {}".format(test_case, count))