import sys
import itertools


input = sys.stdin.readline
N, S = map(int, input().split())
nums = list(map(int, input().split()))
num1 = nums[:len(nums)//2]
num2 = nums[len(nums)//2:]

sum1 = []
for i in range(len(num1) + 1):
    for j in list(itertools.combinations(num1, i)):
        sum1.append(sum(j))

sum2 = []
for i in range(len(num2) + 1):
    for j in list(itertools.combinations(num2, i)):
        sum2.append(sum(j))

sum1.sort()
sum2.sort(reverse=True)

# n, m = first의 길이, second의 길이
n = len(sum1)
m = len(sum2)
i = 0
j = 0
ans = 0
while i < n and j < m:

    # 같은 경우
    if sum1[i] + sum2[j] == S:
        # i,j를 이동
        c1 = 1
        c2 = 1
        i += 1
        j += 1
        # 예외 처리
        while i < n and sum1[i] == sum1[i - 1]:
            c1 += 1
            i += 1
        while j < m and sum2[j] == sum2[j - 1]:
            c2 += 1
            j += 1
        # 전체 순서쌍 반영
        ans += c1 * c2

    # 큰 경우 i만 이동
    elif sum1[i] + sum2[j] < S:
        i += 1

    # 작은 경우 j만 이동
    else:
        j += 1

# s가 0인 경우 공집합의 경우를 빼줘야 하므로 1감소
if  S == 0:
    ans -= 1

# 정답 출력
print(ans)