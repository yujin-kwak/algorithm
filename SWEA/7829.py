T = int(input())

for i in range(1, T + 1):
    n = int(input())
    P = list(map(int, input().split()))

    P.sort()

    ans = P[0] * P[-1]
    print("#{} {}".format(i, ans))