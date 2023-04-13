if __name__=="__main__":
    n, m = map(int,input().split()) # n: 도시(노드)의 수, m: 도로(간선)의 수
    dis = [[5000] * (n+1) for _ in range(n + 1)]

    for i in range(1, n + 1): # 본인 노드에서 본인 노드로 가는 경우 0으로 초기화
        dis[i][i] = 0

    # dis 초기화 (중간에 어떤 정점도 거치지 않고 바로 갔을 때의 최소 비용)
    for i in range(m):
        a, b, c = map(int, input().split())
        dis[a][b] = c

    # k 노드를 거쳐서 i에서 j로 갈 때의 최소 비용 (플로이드 원샬 알고리즘)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    # 출력
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dis[i][j] == 5000:
                print("M", end = ' ')
            else:
                print(dis[i][j], end = ' ')
        print()
