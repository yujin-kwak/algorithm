if __name__=="__main__":
    n = int(input()) # n: 회원의 수
    dis = [[100] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dis[i][i] = 0

    # dis 초기화 (친구이면 1로 변경)
    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        dis[a][b] = 1
        dis[b][a] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    res = [0] * (n + 1) # 각 회원 별 점수
    score = 100 # 회장 후보의 점수
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res[i] = max(res[i], dis[i][j])
        score = min(score, res[i])

    ans = []
    for i in range(1, n + 1):
        if res[i] == score:
            ans.append(i)

    print("{0} {1}".format(score, len(ans)))
    for x in ans:
        print(x, end = ' ')