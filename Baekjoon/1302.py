N = int(input())

words = []
count = [0] * N

for i in range(N):
    word = input()
    if word not in words:
        words.append(word)
    else:
        for j in range(len(words)):
            if words[j] == word:
                count[j] += 1

res = []
for i in range(N):
    if count[i] == max(count):
        res.append(words[i])

res.sort()

print(res[0])