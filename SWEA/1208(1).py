for test_case in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))

    for i in range(N):
        box.sort()
        box[0] += 1
        box[-1] -= 1

    box.sort()
    print("#{} {}".format(test_case, box[-1]-box[0]))