T = int(input())

for test_case in range(1, T + 1):
    number = list(input().split())
    max_v = 0
    min_v = 10000001
    for i in range(10):
        num = list(number[i])
        sum_v = 0
        for j in range(len(num)):
            sum_v += int(num[j])
        max_v = max(max_v, sum_v)
        min_v = min(min_v, sum_v)
    print("#{} {} {}".format(test_case, max_v, min_v))