import sys
input = sys.stdin.readline


def dfs(n, idx, res):
    if idx == N:
        ans = eval(res.replace(" ", ""))
        if ans == 0:
            ans_lst.append(res)
            return
    else:
        n_idx = idx + 1
        dfs(n, n_idx, res + ' ' + str(n_idx))
        dfs(n, n_idx, res + '+' + str(n_idx))
        dfs(n, n_idx, res + '-' + str(n_idx))


T = int(input())
for test_case in range(T):
    N = int(input())

    ans_lst = []
    dfs(N, 1, '1')

    for a in ans_lst:
        print(a)
    print()