'''
[문제 요약]
1부터 N까지의 소수의 개수를 출력하세요.
제한시간 : 1초
'''

N = int(input())
check = [0] * (N+1)

count = 0
for i in range(2, N+1):
    if check[i] == 0:
        count += 1
        for j in range(i, N+1, i):
            check[j] = 1
print(count)
