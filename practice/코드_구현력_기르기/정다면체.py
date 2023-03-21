'''
[문제 요약]
정 N면체와 정 M면체의 두 개의 주사위를 던졌을 때 나올 수 있는 눈의 합 중
확률이 높은 숫자를 출력하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
'''

N, M = map(int,input().split())

count = [0]*(N+M+1)
for i in range(1, N+1):
    for j in range(1, M+1):
        count[i+j] += 1

max = 0
for i in range(N+M+1):
    if count[i] > max:
        max=count[i]

for i in range(N+M+1):
    if count[i] == max:
        print(i, end=' ')