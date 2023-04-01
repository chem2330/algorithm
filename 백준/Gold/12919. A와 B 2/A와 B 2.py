def bfs(lst):
    global flag
    if flag or len(lst) == len(S):
        if lst == S:
            flag = 1
        return
    if lst[-1] == 'A':
        bfs(lst[:-1])
    if lst[0] == 'B':
        bfs(lst[1:][::-1])

S = list(input())
T = list(input())
flag = 0
bfs(T)
print(flag)