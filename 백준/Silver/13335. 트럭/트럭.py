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
    tmp = tmp[1:]
    if sum(tmp) + arr[i] <= L:
        tmp.append(arr[i])
        i += 1
    else:
        tmp.append(0)
    ans += 1
print(ans)