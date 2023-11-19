i = 0
ssum = 0
for _ in range(20):
    a, b, c = input().split()
    if c == 'P':
        continue

    if b == '1.0':
        tmp = 1
    elif b == '2.0':
        tmp = 2
    elif b == '3.0':
        tmp = 3
    else:
        tmp = 4
    i += tmp

    if c == 'A+':
        ssum += tmp * 4.5
    elif c == 'A0':
        ssum += tmp * 4
    elif c == 'B+':
        ssum += tmp * 3.5
    elif c == 'B0':
        ssum += tmp * 3
    elif c == 'C+':
        ssum += tmp * 2.5
    elif c == 'C0':
        ssum += tmp * 2
    elif c == 'D+':
        ssum += tmp * 1.5
    elif c == 'D0':
        ssum += tmp * 1

print(ssum / i)