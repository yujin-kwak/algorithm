T = int(input())
for test_case in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]

    max_len = 0
    for i in range(5):
        max_len = max(max_len, len(arr[i]))

    for i in range(5):
        if len(arr[i]) < max_len:
            j = max_len - len(arr[i])
            for _ in range(j):
                arr[i].append('')

    word = ''
    for i in range(max_len):
        for j in range(5):
            if arr[j][i] == '':
                continue
            else:
                word += arr[j][i]

    print("#{} {}".format(test_case, word))