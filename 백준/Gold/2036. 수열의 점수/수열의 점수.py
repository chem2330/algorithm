import sys


input = sys.stdin.readline

n = int(input())
arr1 = []
arr2 = []
ans = 0
for _ in range(n):
    tmp = int(input())
    if tmp == 1:
        ans += 1
    elif tmp > 0:
        arr1.append(tmp)
    else:
        arr2.append(tmp)
arr1.sort(reverse=True)
arr2.sort()


for i in range(len(arr1) // 2):
    ans += arr1[2 * i] * arr1[2 * i + 1]
if len(arr1) % 2:
    ans += arr1[-1]
for i in range(len(arr2) // 2):
    ans += arr2[2 * i] * arr2[2 * i + 1]
if len(arr2) % 2:
    ans += arr2[-1]
print(ans)