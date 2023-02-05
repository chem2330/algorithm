N, M = map(int, input().split())  # 사람의 수, 파티의 수
know = [0] * (N + 1)
tmp = list(map(int, input().split()))
for i in range(1, tmp[0] + 1):
    know[tmp[i]] = 1
party = [list(map(int, input().split())) for _ in range(M)]
for _ in range(M):
    for i in range(M):
        for j in range(1, party[i][0] + 1):
            if know[party[i][j]]:
                for k in range(1, party[i][0] + 1):
                    know[party[i][k]] = 1
                break

ans = M
for i in range(M):
    for j in range(1, party[i][0] + 1):
        if know[party[i][j]]:
            ans -= 1
            break
print(ans)