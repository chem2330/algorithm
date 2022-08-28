def change(n, k):
    global ans
    if k == 0:
        ans = max(ans, n)
        return
    n_list = list(map(str, str(n)))
    for i in range(len(n_list) - 1):
        for j in range(i + 1, len(n_list)):
            n_list[i], n_list[j] = n_list[j], n_list[i]
            if n_list[0] != '0' and (int(''.join(n_list)), k - 1) not in check:
                check.add((int(''.join(n_list)), k - 1))
                change(int(''.join(n_list)), k - 1)
            n_list[i], n_list[j] = n_list[j], n_list[i]


N, K = map(int, input().split())  # 숫자, 연산 횟수
ans = -1
check = set()
change(N, K)
print(ans)