n = int(input()) # 회의의 수
meeting = [] # n개의 회의

for i in range(n):
    s, e = map(int, input().split()) # s: 시작 시간, e: 끝나는 시간
    meeting.append((s, e)) # 튜플 형태로 저장

meeting.sort(key=lambda x : (x[1], x[0])) # x[1]을 우선으로, x[0]을 차순위로 정렬

end_time = meeting[0][1] # 현재 회의를 했던 끝나는 시간 기록

cnt = 1 # 회의 횟수 기록
for j in range(1, n):
    if meeting[j][0] >= end_time:
        cnt += 1
        end_time = meeting[j][1]

print(cnt)

'''
##### 다른 풀이 #####

end_time = 0 # 현재 회의를 했던 끝나는 시간 기록

cnt = 0 # 회의 횟수 기록
for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1

print(cnt)
'''
