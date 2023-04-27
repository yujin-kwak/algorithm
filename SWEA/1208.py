# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    limit_cnt = int(input()) # 제한된 덤프 횟수
    height = list(map(int, input().split())) # 상자의 높이
    height.sort() # 정렬

    for i in range(limit_cnt):
        # 제한된 덤프 횟수 내에 평탄화가 완료되었을 경우 최고점과 최저점의 높이 차 반환
        if height[0] == height[-1] or height[-1] - height[0] == 1:
            print('#{0} {1}'.format(test_case, height[-1] - height[0]))
            break
        else: # 덤프 진행
            height[0] += 1
            height[-1] -= 1
            height.sort()
    print('#{0} {1}'.format(test_case, height[-1] - height[0]))
