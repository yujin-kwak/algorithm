from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    qu = deque(input().strip())
    left = []
    right = []

    for c in qu:
        if c == '<' and left:
            right.append(left.pop())
        elif c == '>' and right:
            left.append(right.pop())
        elif c == '-' and left:
            left.pop()
        elif c not in {'<', '>', '-'}:
            left.append(c)

    left_res = ''.join(left)
    right_res = ''.join(right[::-1])
    res = left_res + right_res
    print(res)