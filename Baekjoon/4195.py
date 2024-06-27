import sys
input = sys.stdin.readline

def find(x):
    if friends[x] != x:
        friends[x] = find(friends[x])
    return friends[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        friends[b] = a
        number[a] += number[b]

    print(number[a])

T = int(input())
for test_case in range(T):
    friends = {}
    number = {}

    N = int(input())
    for i in range(N):
        a, b = input().split()
        if a not in friends:
            friends[a] = a
            number[a] = 1
        if b not in friends:
            friends[b] = b
            number[b] = 1
        union(a, b)