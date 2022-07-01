A, B, C = map(int, input().split())

AC_list = [[0, C]]
ABC_stack = [[0, 0, C]]
while ABC_stack:
    a, b, c = ABC_stack.pop()
    if a:
        if b != B:
            new_b = b + a
            new_a = 0
            if new_b > B:
                new_a = new_b - B
                new_b = B
            if [new_a, c] not in AC_list:
                AC_list.append([new_a, c])
                ABC_stack.append([new_a, new_b, c])
        if c != C:
            new_c = c + a
            new_a = 0
            if new_c > C:
                new_a = new_c - C
                new_c = C
            if [new_a, new_c] not in AC_list:
                AC_list.append([new_a, new_c])
                ABC_stack.append([new_a, b, new_c])

    if b:
        if a != A:
            new_a = a + b
            new_b = 0
            if new_a > A:
                new_b = new_a - A
                new_a = A
            if [new_a, c] not in AC_list:
                AC_list.append([new_a, c])
                ABC_stack.append([new_a, new_b, c])
        if c != C:
            new_c = c + b
            new_b = 0
            if new_c > C:
                new_b = new_c - C
                new_c = C
            if [a, new_c] not in AC_list:
                AC_list.append([a, new_c])
                ABC_stack.append([a, new_b, new_c])

    if c:
        if a != A:
            new_a = a + c
            new_c = 0
            if new_a > A:
                new_c = new_a - A
                new_a = A
            if [new_a, new_c] not in AC_list:
                AC_list.append([new_a, new_c])
                ABC_stack.append([new_a, b, new_c])
        if b != B:
            new_b = b + c
            new_c = 0
            if new_b > B:
                new_c = new_b - B
                new_b = B
            if [a, new_c] not in AC_list:
                AC_list.append([a, new_c])
                ABC_stack.append([a, new_b, new_c])

answer = []
for a, c in AC_list:
    if a == 0:
        answer.append(c)
print(*sorted(answer))