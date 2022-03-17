N, L = input().split()
cnt = 0
for i in range(1, 10000000):
    if cnt == int(N):
        print(i - 1)
        break
    if L not in str(i):
        cnt += 1
