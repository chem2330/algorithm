N = int(input())
arr = list(map(int, input().split()))

ans = [0] * (max(arr) + 1)
for i in arr:
    ans[i] = max(max(ans[:i]) + 1, ans[i])
print(max(ans))