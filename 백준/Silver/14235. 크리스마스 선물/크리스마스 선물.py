n = int(input())
arr = []
for _ in range(n):
    line = list(map(int, input().split()))
    if line == [0]:
        if arr:
            arr.sort()
            print(arr.pop())
        else:
            print(-1)
    else:
        arr.extend(line[1:])