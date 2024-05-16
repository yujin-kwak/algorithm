T = int(input())
for test_case in range(1, T + 1):
    arr = list(input())
    stack = []
    count = 0

    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append('(')
        elif not stack and arr[i] == '|':
            stack.append('|')
        elif arr[i] == '|' and stack[-1] == '(':
            stack.pop()
            count += 1
        elif arr[i] == ')' and (stack[-1] == '(' or stack[-1] == '|'):
            stack.pop()
            count += 1

    print("#{} {}".format(test_case, count))