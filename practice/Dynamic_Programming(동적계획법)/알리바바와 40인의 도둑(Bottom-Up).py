if __name__=="__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]

    # 직관적으로 알 수 있는 것들 기본적으로 초기화
    dy[0][0] = arr[0][0]
    for i in range(1, n):
        dy[0][i] = dy[0][i-1] + arr[0][i] # 0행 초기화(왼쪽에서밖에 못옴)
        dy[i][0] = dy[i-1][0] + arr[i][0] # 0열 초기화(위쪽에서밖에 못옴)

    # 1행 1열부터 이중 for문을 이용해 다이나믹 값을 구함
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]

    print(dy[n-1][n-1])
