A, B = input().split()

min_cnt = len(B)
for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[j + i]:
            cnt += 1
    min_cnt = min(min_cnt, cnt)
print(min_cnt)