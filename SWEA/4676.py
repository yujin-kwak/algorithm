T = int(input())
for test_case in range(1, T + 1):
    in_str = list(input())
    H = int(input())
    location = list(map(int, input().split()))

    location.sort(reverse=True)

    for i in range(H):
        in_str.insert(location[i], '-')

    res = ''.join(in_str)
    print("#{}".format(test_case), res)