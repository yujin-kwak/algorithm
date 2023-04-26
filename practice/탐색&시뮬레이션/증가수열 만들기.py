'''
from collections import deque
n = int(input()) # 수열의 길이
num = list(map(int, input().split())) # 받아온 수열
new_num = sorted(num) # 정렬된 수열
num = deque(num)

cnt = 0 # 최대 증가수열의 길이
res = '' # L과 R로 이루어진 문자열
for i in range(n):
    if new_num[i] == num[0]: # 현재 가장 작은 값이 왼쪽과 같은 경우
        num.popleft()
        cnt += 1
        res += 'L'
    elif new_num[i] == num[-1]: # 현재 가장 작은 값이 오른쪽과 같은 경우
        num.pop()
        cnt += 1
        res += 'R'
    else:
        continue

print(cnt)
print(res)
'''

######## 다른 풀이 #########
n = int(input()) # 수열의 길이
num = list(map(int, input().split())) # 받아온 수열

lt = 0 # 수열의 맨 왼쪽
rt = n - 1 # 수열의 맨 오른쪽
last = 0 # 현재 증가수열의 마지막 값
res = '' # L과 R로 이루어진 문자열
tmp = [] # 두개의 값을 넣어서 정렬할 리스트

while lt <= rt:
    if num[lt] > last:
        tmp.append((num[lt], 'L'))
    if num[rt] > last:
        tmp.append((num[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0: # lt와 rt가 모두 last보다 작을 때
        break
    else:
        last = tmp[0][0]
        res += tmp[0][1]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
        tmp.clear() # tmp를 비움

print(len(res))
print(res)