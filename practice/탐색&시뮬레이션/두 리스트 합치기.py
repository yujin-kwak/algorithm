n = int(input())
arr1 = list(map(int, input().split())) # 첫번째 리스트
m = int(input())
arr2 = list(map(int, input().split())) # 두번째 리스트

p1 = 0 # arr1의 지점을 가리키는 변수
p2 = 0 # arr2의 지점을 가리키는 변수
res = [] # 최종 리스트

while p1 < n and p2 < m: # p1이나 p2가 n, m까지 갔다면 해당 리스트를 다 처리한 것
    if arr1[p1] <= arr2[p2]:
        res.append(arr1[p1])
        p1 += 1
    else:
        res.append(arr2[p2])
        p2 += 1

if p1 < n: # p1이 n보다 작으면 arr1이 남은 것
    res = res + arr1[p1:]
if p2 < m: # p2가 m보다 작으면 arr2가 남은 것
    res = res + arr2[p2:]

print(*res)

'''
# sort 사용 - 시간복잡도 nlogn
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr = arr1 + arr2
arr.sort()
print(*arr)
'''