s = input() # 입력된 문자열
res = 0 # 추출한 숫자로 만들어진 자연수
for x in s:
    if x.isdecimal(): # 0 ~ 9사이의 숫자일 경우
        res = res * 10 + int(x)
print(res)

# 만들어진 자연수의 약수 개수 구하기
cnt = 0
for i in range(1, res + 1):
    if res % i == 0: # i가 res의 약수이면 cnt + 1을 함
        cnt += 1
print(cnt)