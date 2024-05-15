T = int(input())
for test_case in range(1, T + 1):
    score = list(map(int, input().split()))
    sum_v = 0

    for i in range(len(score)):
        if score[i] < 40:
            score[i] = 40
        sum_v += score[i]

    res = int(sum_v / len(score))
    print("#{} {}".format(test_case, res))