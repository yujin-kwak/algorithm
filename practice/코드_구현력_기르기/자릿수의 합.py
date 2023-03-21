'''
[문제 요약]
N개의 자연수가 입력됩니다.
각 자연수의 자릿수 합을 구하고, 그 합이 가장 큰 수를 출력하세요.
digit_sum(x)를 꼭 작성해서 구현해주세요.
'''

N = int(input())
number = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x>0 :
        sum += x%10
        x = x//10
    return sum

max = 0
answer = 0
for x in number:
    total = digit_sum(x)
    if total > max:
        max = total
        answer = x
print(answer)

''' 
# 문자열로 처리하여 자릿수 더하는 방법
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum+=int(i)
    return sum
'''