def bfs(i, height):
    global min_value
    if height >= B:
        min_value = min(min_value, height)
        return
    
    if i == N:
        return
    
    bfs(i+1, height + H[i])
    bfs(i+1, height)


T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int,input().split()))

    min_value = 200001
    bfs(0, 0)
    
    print('#{} {}'.format(test_case, min_value - B))