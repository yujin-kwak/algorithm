for test_case in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))

    tot = 0 # 조망권을 확보한 세대의 총 수
    for i in range(2, n-2):
        # 왼쪽 2개의 공간과 오른쪽 2개의 공간 중 최댓값을 구함
        temp = max(building[i-1], building[i-2], building[i+1], building[i+2])
        if building[i] > temp: # 최댓값이 현재 빌딩 높이보다 크면 조망권 확보 못한것.
            tot += (building[i] - temp) # 현재 빌딩 높이에서 최댓값을 뺀만큼 조망권 확보한 것.

    print('#{0} {1}'.format(test_case, tot))