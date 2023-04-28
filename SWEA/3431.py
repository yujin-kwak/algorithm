T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    if L <= X <= U: # 적정량의 운동을 했을 경우
        print('#{0} {1}'.format(test_case, 0))
    elif X < L: # 적정량보다 운동을 적게 했을 경우
        print('#{0} {1}'.format(test_case, L-X))
    else: # 적정량보다 운동을 많이 했을 경우
        print('#{0} {1}'.format(test_case, -1))