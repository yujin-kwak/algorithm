for test_case in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    for i in range(N):
        stack = []
        for j in range(N):
            if not stack and board[j][i] == 1:
                stack.append(1)
            if stack and board[j][i] == 2:
                count += 1
                stack.pop()

    print("#{} {}".format(test_case, count))