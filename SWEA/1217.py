test_case = int(input())

N, M = map(int, input().split())

def mul(n, m):
    if m == 0:
        return 1

    return int(n) * mul(n, m - 1)

print("#{} {}".format(test_case, mul(N, M)))