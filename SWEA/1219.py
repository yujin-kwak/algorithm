def graph(v):
    visited[v] = 1
    for i in G[v]:
        if not visited[i]:
            graph(i)
    return

for test_case in range(1, 11):
    T, E = map(int, input().split()) #test_case번호, 간선 개수
    arr = list(map(int, input().split())) #입력 받기

    visited = [0] * 100
    G = [[] for _ in range(100)] #갈 수 있는 길 표시
    for i in range(E):
        G[arr[2*i]].append(arr[2*i+1])
    graph(0)

    print("#{} {}".format(T, visited[99]))