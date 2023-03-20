'''
[문제 요약]
1~100사이의 자연수가 적힌 N장의 카드 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록합니다.
모든 경우를 기록한 값 중 K번째로 큰 수를 출력하세요.
N장의 카드에는 같은 숫자의 카드가 있을 수 있고, 중복된 숫자는 무시 해야함.
ex) 만들어진 수 : 25 25 23 23 22 20 19 => K=3 : 22
'''
import sys

N, K = map(int,input().split())
num = list(map(int,sys.stdin.readline().rstrip().split()))
res = set()

for i in range(N) :
    for j in range(i + 1, N) :
        for m in range(j + 1, N) :
            res.add(num[i] + num[j] + num[m])

res=list(res)
res.sort(reverse=True)
print(res[K-1])
