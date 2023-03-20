'''
[문제 요약]
N개의 숫자로 이루어진 숫자열 중 s번째에서 e번째 까지의 수를 오름차순 정렬했을 때,
정렬된 숫자들 중 k번째의 숫자를 출력하시오.
ex)
6 2 5 3
5 2 7 3 8 9
=> 7
'''

import sys

T = int(input())
for i in range (T) :
    N, s, e, k = map(int, input().split())
    num = list(map(int,sys.stdin.readline().rstrip().split()))
    num_list = num[s-1 : e]
    num_list.sort()
    print("#{0} {1}".format(i + 1 , num_list[k-1]))