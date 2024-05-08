T = int(input())
for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    
    if L <= X <= U:
        res = 0
    elif X < L:
        res = L - X
    else:
        res = -1
    
    print('#{} {}'.format(test_case, res))