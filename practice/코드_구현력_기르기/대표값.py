'''
[문제 요약]
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생이 몇번째인지 출력하세요.
평균과 가장 가까운 점수가 여러 개일 경우 점수가 높은 학생의 번호를 출력하세요.
높은 점수를 가진 학생이 여러 명일 경우 더 먼저 있는 학생의 번호를 출력하세요.
'''

n = int(input())
number = list(map(int, input().split()))
average = int((sum(number) / n) + 0.5) #파이썬에서는 sum을 사용하면 리스트의 모든 값을 더할 수 있다.

abs_min = float('inf')
k=0
for i in range (n):
    if abs(average - number[i]) < abs_min :
        abs_min = abs(average - number[i])
        k = i
    if abs(average - number[i]) == abs_min :
        if number[i] > number[k] :
            k = i

print(average, k+1)
