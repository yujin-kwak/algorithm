import sys

input = sys.stdin.readline
N = int(input())
poem = dict() #poem: 빈 딕셔너리

for i in range(N):
    word = input().rstrip()
    poem[word] = 1 #key: word, value: 1

for i in range(N-1):
    word = input().rstrip()
    poem[word] = 0

for key, value in poem.items():
    if value == 1:
        print(key)
        break
