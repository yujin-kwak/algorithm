from collections import deque

T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())

    document = deque()

    tmp = map(int, input().split())
    for i in tmp:
        document.append(i)

    result = 1
    while document:
        if document[0] < max(document):
            document.append(document.popleft())
        else:
            if M == 0:
                break
            document.popleft()
            result += 1
        if M > 0:
            M -= 1
        else:
            M = len(document) - 1

    print(result)