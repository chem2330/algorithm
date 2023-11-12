T = int(input())
cnt0 = [1, 0, 1]
cnt1 = [0, 1, 1]

for _ in range(T):
    for i in range(3, 41):
        cnt0.append(cnt0[i - 2] + cnt0[i - 1])
        cnt1.append(cnt1[i - 2] + cnt1[i - 1])
    N = int(input())
    print(cnt0[N], cnt1[N])