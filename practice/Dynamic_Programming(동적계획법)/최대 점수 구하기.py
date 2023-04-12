if __name__=="__main__":
    n, m = map(int, input().split()) # n: 문제의 개수, m: 제한 시간
    dy = [0] * (m + 1)

    for i in range(n):
        ps, pt = map(int, input().split()) # ps: 점수, pt: 푸는데 걸리는 시간
        for j in range(m, pt - 1, -1):
            dy[j] = max(dy[j], dy[j - pt] + ps)

    print(dy[m])