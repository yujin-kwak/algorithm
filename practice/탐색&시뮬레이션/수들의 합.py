n, m = map(int, input().split()) # n: n개의 수로 된 수열, m: i~j의 합이 m이 되는 경우 구하기
num = list(map(int, input().split()))

lt = 0
rt = 1
tot = num[0] # lt부터 rt 바로 전까지의 합
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += num[rt]
            rt += 1
        else: # rt가 n이면 break
            break
    elif tot == m:
        cnt += 1
        tot -= num[lt]
        lt += 1
    else:
        tot -= num[lt]
        lt += 1

print(cnt)