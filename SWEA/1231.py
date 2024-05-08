def in_order(n):
    global word
    if n <= N :
        in_order(n * 2)
        word += arr[n-1][1]
        in_order(n * 2 + 1)

for test_case in range(1, 11):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    word = ''
    in_order(1)
    print('#{} {}'.format(test_case, word))