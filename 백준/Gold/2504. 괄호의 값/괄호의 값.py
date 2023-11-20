char = list(input())
q = []
cal = []
flag = 0

for c in char:
    if c == '(':
        q.append(2)
    elif c == '[':
        q.append(3)
    elif c == ')':
        if q and q[-1] == 2:
            cal.append([len(q), q[-1]])
            q.pop()
        else:
            flag = 1
            break
    elif c == ']':
        if q and q[-1] == 3:
            cal.append([len(q), q[-1]])
            q.pop()
        else:
            flag = 1
            break

if q:
    flag = 1

if flag == 1:
    print(0)

else:
    ans = [0 for _ in range(16)]
    ans[cal[0][0]] = cal[0][1]

    for i in range(1, len(cal)):
        a1, b1 = cal[i - 1][0], cal[i - 1][1]
        a2, b2 = cal[i][0], cal[i][1]
        if a1 <= a2:
            ans[a2] += b2
        elif a1 > a2:
            ans[a2] += ans[a1] * b2
            ans[a1] = 0

    print(ans[1])