for test_case in range(1, 11):
    N, in_str = input().split()

    stack = []
    for i in range(int(N)):
       if not stack or in_str[i] != stack[-1]:
           stack.append(in_str[i])
       else:
           stack.pop()

    print("#{} {}".format(test_case, ''.join(stack)))
