def check(paper, n):
    global white, blue
    total = 0
    for i in range(n):
        total += sum(paper[i])
    if total == 0:
        white += 1
    elif total == n ** 2:
        blue += 1
    elif n == 1:
        return
    else:
        paper1 = []
        paper2 = []
        paper3 = []
        paper4 = []
        new_n = n // 2
        for x in range(new_n):
            paper1.append(paper[x][:new_n])
            paper2.append(paper[x][new_n:])
        for x in range(new_n, n):
            paper3.append(paper[x][:new_n])
            paper4.append(paper[x][new_n:])
        check(paper1, new_n)
        check(paper2, new_n)
        check(paper3, new_n)
        check(paper4, new_n)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0
check(arr, N)
print(white)
print(blue)
