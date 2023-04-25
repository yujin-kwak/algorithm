n = int(input()) # n: 지원자 수
people = [] # 지원자들의 키와 몸무게 정보

for i in range(n):
    h, w = map(int, input().split()) # h: 키, w: 몸무게
    people.append((h, w)) # 튜플 형태로 저장

people.sort(reverse=True) # 키를 기준으로 내림차순 정렬

max_w = 0 # 최대 몸무게
cnt = 0 # 뽑힌 인원 수

for h, w in people:
    if w > max_w: # 몸무게가 지금까지의 몸무게 중 최댓값보다 큰 경우만 cnt + 1
        max_w = w
        cnt += 1

print(cnt)
