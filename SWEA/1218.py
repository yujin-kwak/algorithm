for test_case in range(1, 11):
    N = int(input())
    arr = list(input())
    stack = []

    for i in range(N):
        if not stack or arr[i] == '(' or arr[i] == '[' or arr[i] == '{' or arr[i] == '<':
            stack.append(arr[i])
        elif arr[i] == ')' and stack[-1] == '(':
            stack.pop()
        elif arr[i] == ']' and stack[-1] == '[':
            stack.pop()
        elif arr[i] == '}' and stack[-1] == '{':
            stack.pop()
        elif arr[i] == '>' and stack[-1] == '<':
            stack.pop()
        else:
            stack.append(arr[i])

    if stack:
        res = 0
    else:
        res = 1

    print("#{} {}".format(test_case, res))