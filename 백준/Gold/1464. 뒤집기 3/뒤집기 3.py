ans = input()
arr = list(ans)
s1 = arr[0]
for i in range(1, len(arr)):
    if s1[i-1] < arr[i]:
        s1 = arr[i]+s1
    else:
        s1 = s1+arr[i]
print(s1[::-1])