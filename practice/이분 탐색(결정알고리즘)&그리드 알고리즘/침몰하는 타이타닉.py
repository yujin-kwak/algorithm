from collections import deque

n, m = map(int, input().split()) # n: 승객의 인원, m: 보트에 탈 수 있는 최대 무게
weight = list(map(int, input().split())) # 승객별 몸무게
weight.sort() # 오름차순 정렬
weight = deque(weight)

cnt = 0 # 보트의 수
while weight:
    if len(weight) == 1: # 마지막에 한명만 남으면 혼자 타게 함
        cnt += 1
        break
    # 남아있는 승객 중 가장 가벼운 사람과 무거운 사람의 몸무게를 더했을 때 m보다 크면
    # 가장 무거운 사람 혼자 타고 감
    if (weight[0] + weight[-1]) > m:
        weight.pop()
        cnt += 1

    else: # 그렇지 않으면 두명이 같이 타고 감
        weight.popleft()
        weight.pop()
        cnt += 1

print(cnt)
'''
5 140
90 50 70 100 60
'''