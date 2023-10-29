import itertools


while True:
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        break

    arr = tmp[1:]
    combs = itertools.combinations(arr, 6)
    for com in combs:
        print(*com)
    print()