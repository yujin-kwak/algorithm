# Top-Down방식은 재귀함수와 메모이제이션 이용하여 품

def DFS(len):
    if dy[len] > 0: # 이미 구한 값이면 cut edge
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]

if __name__=="__main__":
    n = int(input())
    dy = [0] * (n+1)
    print(DFS(n))