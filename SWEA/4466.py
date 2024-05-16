T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))

    score.sort(reverse=True)

    sum_score = 0
    for i in range(K):
        sum_score += score[i]

    print("#{} {}".format(test_case, sum_score))