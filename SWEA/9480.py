T = int(input())
eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def dfs(i, word):
    global count
    new_word = sorted(word)
    if new_word == eng:
        count += 1

    dfs(i+1, word.append(*arr[i]))
    dfs(i+1, word)

for test_case in range(1, T + 1):
    N = int(input())
    count = 0
    arr = []
    for i in range(N):
        arr.append(list(input()))
    print(arr)
    dfs(0, [])


    
# T = int(input())
#
# def check(string): # 소문자 26개가 다 있으면 True 리턴
#
#     answer = "abcdefghijklmnopqrstuvwxyz"
#     string = list(set(string))
#
#     cnt = 0
#     for st_ in string:
#         if st_ in answer:
#             cnt += 1
#
#     if cnt == 26:
#         return True
#     return False
#
# def dfs(idx, depth, string): # 조합을 구현하여 단어를 이어 붙힘
#     global answer
#
#     if check(string):
#         answer += 1
#
#     if depth == N:
#         return
#
#     for i in range(idx, N):
#         dfs(i+1, depth+1, string+alpha[i])
#
# for tc in range(1, T+1):
#
#     N = int(input())
#     alpha = [ input() for _ in range(N) ]
#     answer = 0
#
#     dfs(0, 0, "")
#
#     print(f"#{tc}", answer)