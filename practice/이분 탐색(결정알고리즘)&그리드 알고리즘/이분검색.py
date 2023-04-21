n, m = map(int, input().split())
num = list(map(int, input().split())) # 리스트 값 받아오기
num.sort() # 오름차순 정렬

lt = 0 # 왼쪽 맨 끝
rt = n - 1 # 오른쪽 맨 끝

while lt <= rt:
    mid = (lt + rt) // 2
    if num[mid] == m: # num[mid]값이 m이면 찾은 것이므로 mid + 1 출력
        print(mid + 1)
        break
    elif num[mid] > m: # num[mid]값이 m보다 크면 m은 mid보다 작은쪽(왼쪽)에 있는 것
        rt = mid - 1
    else: # num[mid]값이 m보다 크면 m은 mid보다 큰쪽(오른쪽)에 있는 것
        lt = mid + 1