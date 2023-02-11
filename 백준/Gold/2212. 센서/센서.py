N = int(input())  # 센서의 개수
K = int(input())  # 집중국의 개수
arr = sorted(map(int, input().split()))  # 센서의 좌표
gaps = []
for i in range(len(arr) - 1):
    gaps.append(arr[i+1] - arr[i])
gaps.sort()
print(arr[-1] - arr[0] - sum(gaps[N-K:]))