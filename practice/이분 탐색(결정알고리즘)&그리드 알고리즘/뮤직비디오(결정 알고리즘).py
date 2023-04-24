def count_fn(capacity):
    cnt = 1 # DVD 필요한 개수
    sum_music = 0 # DVD에 저장한 노래들을 합함

    for x in music:
        if (sum_music + x) > capacity:
            cnt += 1
            sum_music = x
        else:
            sum_music += x

    return cnt

n, m = map(int, input().split()) # n: 곡의 개수, m: 곡을 담을 DVD 개수
music = list(map(int, input().split())) # 각 곡의 길이
max_len_music = max(music) # 곡들 중 가장 긴 것

lt = 1 # 범위의 왼쪽 지점
rt = sum(music) # 범위의 오른쪽 지점
res = 0 # DVD의 최소 용량 크기

while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= max_len_music and count_fn(mid) <= m: # DVD 용량이 곡의 최대 길이보다 크고 DVD m개로 n개의 곡을 담을 수 있는 경우
        res = mid
        rt = mid - 1 # 해당 값보다 큰 값은 가능, 더 좋은 답 찾기
    else:
        lt = mid + 1 # 해당 값보다 작은 값은 불가능

print(res)