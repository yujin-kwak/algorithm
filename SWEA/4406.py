T = int(input())

for test_case in range(1, T + 1):
    arr = ['a', 'e', 'i', 'o', 'u']
    word = list(input())

    res = ''
    for i in range(len(word)):
        if word[i] in arr:
            res += ''
        else:
            res += word[i]
    
    print(res)
    