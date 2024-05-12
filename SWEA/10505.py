T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    sum_v = 0

    num = list(map(int,input().split()))
    res = sum(num) / N

    ans = 0
    for i in range(N):
        if num[i] <= res:
            ans += 1
        

    print("#{} {}".format(test_case, ans))