import sys
input = sys.stdin.readline

doc = input().strip()
word = input().strip()

count = 0
idx = 0

while len(doc) - idx >= len(word):
    if doc[idx:idx+len(word)] == word:
        count += 1
        idx += len(word)
    else:
        idx += 1

print(count)