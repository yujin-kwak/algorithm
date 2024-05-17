T = int(input())

def dfs(idx, num, select):
    global res
    if select == 3:
        if num not in res:
            res.append(num)
            return
    if idx == len(number):
        return
    dfs(idx+1, num + number[idx], select + 1)
    dfs(idx+1, num, select)

for test_case in range(1, T + 1):
    res = []
    number = list(map(int, input().split()))

    dfs(0, 0, 0)
    res.sort(reverse=True)
    print("#{} {}".format(test_case, res[4]))