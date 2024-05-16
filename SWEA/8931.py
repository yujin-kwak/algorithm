T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    stack = []
    for i in range(N):
        money = int(input())
        if money != 0:
            stack.append(money)
        else:
            stack.pop()

    res = sum(stack)
    print("#{} {}".format(test_case, res))