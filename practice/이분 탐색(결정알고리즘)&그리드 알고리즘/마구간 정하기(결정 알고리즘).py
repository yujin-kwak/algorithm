def check(length):
    cnt = 1 # 배치한 말의 수
    ep = xi[0] # 첫 번째 마구간에 첫번째 말 배치
    for i in range(1, n):
        if (xi[i] - ep) >= length: # 다음 마구간과 ep의 차가 length보다 크면 배치 가능
            cnt += 1 # 배치한 말의 수 증가
            ep = xi[i] # ep 지점 변경
    return cnt

n, c = map(int, input().split()) # n: 마구간 개수, c: 현수가 가지고 있는 말
xi = [] # 마구간 좌표
for _ in range(n):
    temp = int(input())
    xi.append(temp)
xi.sort()

lt = 1
rt = xi[n-1]

while lt <= rt:
    mid = (lt + rt) // 2
    if check(mid) >= c: # 답으로 가능한 경우
        res = mid
        lt = mid + 1 # 더 짧은 거리는 가능, 작은 부분은 보지 않고 큰 부분을 봄
    else: # 답으로 가능하지 않은 경우
        rt = mid - 1 # 더 큰 값은 불가능, 작은 부분을 봄

print(res)