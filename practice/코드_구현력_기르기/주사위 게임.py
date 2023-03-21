'''
[문제 요약]
1~6의 눈을 가진 주사위 3개를 던져 다음과 같은 규칙에 따라 상금을 받습니다.
1) 같은 눈이 3개 나오면 10,000 + (같은 눈) * 1,000원의 상금을 받습니다.
2) 같은 눈이 2개만 나오면 1,000 + (같은 눈) * 100원의 상금을 받습니다.
1) 모두 다른 눈이 나오면 (가장 큰 눈) * 100원의 상금을 받습니다.
가장 많은 상금을 받은 사람의 상금을 출력하세요.
'''

import sys

N = int(input())
max_money=0

for i in range(N):
    temp = sys.stdin.readline().rstrip().split()
    temp.sort(reverse=True)
    a, b, c = map(int, temp)

    if a==b and b==c:
        money = 10000 + a * 1000
    elif a==b or a==c:
        money = 1000 + a * 100
    elif b==c:
        money = 1000 + b * 100
    else:
        money = a * 100
    if money > max_money:
        max_money = money

print(max_money)