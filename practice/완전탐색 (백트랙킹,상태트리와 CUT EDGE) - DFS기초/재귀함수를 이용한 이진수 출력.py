'''
[문제 요약]
입력되는 10진수 N을 2진수로 변환하여 출력하세요.
재귀함수를 꼭 이용하여 구현하세요.
'''

N = int(input())

i = 0
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x % 2, end ='')

DFS(N)