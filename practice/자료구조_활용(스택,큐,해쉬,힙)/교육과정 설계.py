from collections import deque

essential = input()
N = int(input())

for i in range(N):
    plan = input()
    dq = deque(essential)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#{0} NO".format(i + 1))
                break

    else:
        if dq:
            print("#{0} NO".format(i + 1))
        else:
            print("#{0} YES".format(i + 1))
