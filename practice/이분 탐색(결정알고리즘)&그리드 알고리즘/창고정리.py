L = int(input()) # 창고의 가로 길이
height = list(map(int, input().split())) # 각 높이
M = int(input()) # 높이 조정 횟수
height.sort() # 오름차순 정렬

for _ in range(M):
    height[0] += 1 # 가장 작은 값 + 1
    height[L-1] -= 1 # 가장 큰 값 - 1
    height.sort()

print(height[L-1] - height[0]) # 가장 큰 값 - 장 작은 값

'''
10
69 42 68 76 40 87 14 65 76 81
'''