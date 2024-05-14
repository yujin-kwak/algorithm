T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = []
    for i in range(1, N + 1):
        if i not in arr:
            ans.append(i)

    print("#{}".format(test_case), *ans)