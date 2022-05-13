w, s = map(int, input().split())  # 찾고자 하는 단어의 길이 / 추출한 단어의 길이
W = input()
S = input()

word = {}
for elem in W:
    if word.get(elem):
        word[elem] += 1
    else:
        word[elem] = 1

search = {}
for i in range(w):
    if search.get(S[i]):
        search[S[i]] += 1
    else:
        search[S[i]] = 1

if word == search:
    cnt = 1
else:
    cnt = 0

i = w
while i < s:
    if search.get(S[i]):
        search[S[i]] += 1
    else:
        search[S[i]] = 1
    if search[S[i - w]] == 1:
        del search[S[i - w]]
    else:
        search[S[i - w]] -= 1
    if word == search:
        cnt += 1
    i += 1

print(cnt)