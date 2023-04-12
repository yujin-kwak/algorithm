if __name__=="__main__":
    n = int(input()) # 동전 종류의 개수
    coin = list(map(int, input().split())) # 동전의 종류
    m = int(input()) # 거슬러 줄 금액

    # dy 초기화
    dy = [1000] * (m + 1)
    dy[0] = 0 # 0원을 거슬러 주는 데 필요한 동전의 개수: 0

    for i in range(n):
        for j in range(coin[i], m + 1):
            dy[j] = min(dy[j], dy[j - coin[i]] + 1) # 기존 dy와 현재 동전을 적용했을 때 중 더 작은 것을 선택

    print(dy[m])