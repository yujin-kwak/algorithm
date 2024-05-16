for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    input_N = int(input())
    input_arr = list(input().split())
    x = 0
    y = 0

    for i in range(len(input_arr)):
        if input_arr[i] == 'I':
            x = int(input_arr[i + 1])
            y = int(input_arr[i + 2])
            insert_arr = input_arr[i+3:i+3+y]
            for j in range(y):
                arr.insert(x, int(insert_arr[j]))
                x += 1

        if input_arr[i] == 'D':
            x = int(input_arr[i + 1])
            y = int(input_arr[i + 2])
            for j in range(y):
                arr.pop(x)

    ans = []
    for i in range(10):
        ans.append(arr[i])

    print("#{}".format(test_case), *ans)
