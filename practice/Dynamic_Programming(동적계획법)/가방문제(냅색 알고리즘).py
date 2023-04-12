if __name__=="__main__":
    n, max_w = map(int,input().split())
    dy = [0] * (max_w + 1)

    for i in range(n):
        w, v = map(int, input().split())
        for j in range(w, max_w + 1): # 보석의 무게부터 돌려야함. 그렇지 않으면 (j - w)에서 음수 인덱스를 돌게됨.
            dy[j] = max(dy[j], dy[j - w] + v) # 기존 dy와 현재 보석을 넣는다고 했을 때 중 더 큰 것을 선택

    print(dy[max_w])