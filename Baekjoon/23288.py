dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

top, bottom, front, back, left, right = 1, 6, 5, 2, 4, 3

N, M, K = map(int, input().split())
map_data = [list(map(int, input().split()))for _ in range(N)]

y, x, d = 0, 0, 0
score = 0


def dice_map(d):
    global top, bottom, front, back, left, right
    if d == 0:
        tmp_left, tmp_top, tmp_right, tmp_bottom = left, top, right, bottom
        left, top, right, bottom = tmp_bottom, tmp_left, tmp_top, tmp_right
    elif d == 1:
        tmp_back, tmp_top, tmp_front, tmp_bottom = back, top, front, bottom
        back, top, front, bottom = tmp_bottom, tmp_back, tmp_top, tmp_front
    elif d == 2:
        tmp_left, tmp_top, tmp_right, tmp_bottom = left, top, right, bottom
        left, top, right, bottom = tmp_top, tmp_right, tmp_bottom, tmp_left
    elif d == 3:
        tmp_back, tmp_top, tmp_front, tmp_bottom = back, top, front, bottom
        back, top, front, bottom = tmp_top, tmp_front, tmp_bottom, tmp_back

def score_DFS(y, x):
    global max_cnt,visit
    max_cnt += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and map_data[ny][nx] == B:
            if visit[ny][nx] == 0:
                visit[ny][nx] = 1
                score_DFS(ny, nx)
    return

def direction(A, B, d):
    if A > B:
        return (d + 1) % 4
    elif A < B:
        return (d - 1) % 4
    else:
        return d

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    for _ in range(K):

        # 주사위 이동
        if 0 <= y + dy[d] < N and 0 <= x + dx[d] < M:
            d = d
        else:
            d = (d + 2) % 4
        y, x = y + dy[d], x + dx[d]

        # 주사위 굴리기
        dice_map(d)

        # 점수 계산
        A = bottom
        B = map_data[y][x]
        visit = [[0 for _ in range(M)]for _ in range(N)]
        visit[y][x] = 1
        max_cnt = 0
        score_DFS(y, x)
        score += max_cnt * B

        # 이동 방향 결정
        d = direction(A, B, d)
    # ///////////////////////////////////////////////////////////////////////////////////
