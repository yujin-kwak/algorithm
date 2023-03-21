'''
[문제 요약]
N개의 자연수가 입력됩니다.
각 자연수를 뒤집은 수가 소수이면 그 수를 출력하세요.
910을 뒤집으면 19로 숫자화 해야합니다. 첫자리부터 연속된 0은 무시합니다.
def reverse(x)와 def isPrime(x)를 반드시 작성해서 구현해주세요.
'''

N = int(input())
number = map(int, input().split())

def reverse(x):
    res = 0
    while x > 0:
        temp = x % 10
        res = res * 10 + temp
        x = x // 10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0 :
            return False
    else:
        return True

for i in number:
    temp = reverse(i)
    if isPrime(temp):
        print(temp, end=' ')