T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    sum_value  = A + B

    while(True):
        if sum_value < 24:
            break
        else:
            sum_value -= 24
            
    print('#{} {}'.format(test_case, sum_value))