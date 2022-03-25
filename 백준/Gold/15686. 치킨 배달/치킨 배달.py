import itertools


N, M = map(int, input().split())  # 행렬 크기, 치킨집 수
arr = [list(map(int, input().split())) for _ in range(N)]
home_list = []
chicken_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home_list += [[i, j]]
        elif arr[i][j] == 2:
            chicken_list += [[i, j]]
min_dis = 2000
chicken_combinations = itertools.combinations(chicken_list, M)
for chicken_com in chicken_combinations:
    total = 0
    for home in home_list:
        tmp = []
        for chicken in chicken_com:
            tmp += [abs(home[0]-chicken[0]) + abs(home[1]-chicken[1])]
        total += min(tmp)
    if total < min_dis:
        min_dis = total
print(min_dis)