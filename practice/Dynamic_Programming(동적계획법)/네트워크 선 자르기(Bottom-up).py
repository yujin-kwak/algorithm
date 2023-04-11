N = int(input())
dy = [0] * (N+1) #0번 인덱스 사용 안하고 1번부터 사용하기 위해

dy[1] = 1 # 1m짜리 하나로 자르는 방법 밖에 없음
dy[2] = 2 # 1m + 1m / 2m짜리 하나로 자르는 방법

for i in range(3, N+1): # 3m짜리부터 Dynamic으로 구함
    dy[i] = dy[i-1] + dy[i-2]

print(dy[N])