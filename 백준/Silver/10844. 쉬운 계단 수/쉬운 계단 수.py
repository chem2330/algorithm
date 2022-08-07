N = int(input())


cnt = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for _ in range(1, N):
    tmp = cnt[:]
    cnt[0] = tmp[1]
    cnt[9] = tmp[8]
    for i in range(1, 9):
        cnt[i] = tmp[i - 1] + tmp[i + 1]


print(sum(cnt) % 1000000000)