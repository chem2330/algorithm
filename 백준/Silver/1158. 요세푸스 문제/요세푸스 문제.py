N, K = map(int, input().split())
left = [0, N] + list(range(1, N))
right = [0] + list(range(2, N + 1)) + [1]
# left = [0, 7, 1, 2, 3, 4, 5, 6]
# right = [0, 2, 3, 4, 5, 6, 7, 1]

results = [K]
now = K
right[left[K]] = right[K]
left[right[K]] = left[K]

for _ in range(N - 1):
    for _ in range(K):
        now = right[now]
    results.append(now)
    right[left[now]] = right[now]
    left[right[now]] = left[now]

print('<' + str(results)[1:-1] + '>')