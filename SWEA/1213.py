for test_case in range(10):
    T = int(input())
    search = input()
    in_str = input()

    cnt = 0
    for i in range(len(in_str)):
        if in_str[i] == search[0]:
            if in_str[i:i+len(search)] == search:
                cnt += 1

    print("#{} {}".format(T, cnt))