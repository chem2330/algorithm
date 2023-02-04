n, w, L = map(int, input().split())  # 다리를 건너는 트럭 수, 다리의 길이, 다리의 최대하중
arr = list(map(int, input().split()))

tmp = [0] * w
tmp[-1] = arr[0]
i = 1
ans = 1
while True:
    if i == n:
        ans += w
        break
    if sum(tmp[1:]) + arr[i] <= L:
        tmp = tmp[1:] + [arr[i]]
        i += 1
    else:
        tmp = tmp[1:] + [0]
    ans += 1
print(ans)