def DFS(x, y):
    if dy[x][y] > 0: #이미 구한 값인 경우 cut-edge
        return dy[x][y]

    if x == 0 and y == 0: # 출발 지점, 여기까지만 호출해야 함.(재귀의 종료지점)
        return arr[0][0]

    else:
        if y == 0: #열 좌표가 0이면, 위쪽으로만 가야함
            dy[x][y] = DFS(x - 1, y) + arr[x][y]
        elif x == 0: #행 좌표가 0이면, 왼쪽으로만 가야함
            dy[x][y] = DFS(x, y - 1) + arr[x][y]
        else: # 왼쪽과 위쪽 중 작은 경우 선택
            dy[x][y] = min(DFS(x - 1, y), DFS(x, y - 1)) + arr[x][y]
        return dy[x][y]

if __name__=="__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    print(DFS(n-1, n-1))