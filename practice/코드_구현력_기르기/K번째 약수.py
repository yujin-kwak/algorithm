'''
[문제 요약]
N의 약수 중 K번째로 작은 수를 출력하세요.
K번째 약수가 존재하지 않을 경우 -1을 출력하세요.
'''

N, K = map(int,input().split())
count=0

for i in range(1, N+1):
    if N % i == 0 :
        count += 1
    if count == K :
        print(i)
        break
else :
    print(-1)


