N = int(input())
n = 666

while True:
    tmp = str(n)
    if '666' in tmp:
        N -= 1
    if N == 0:
        print(n)
        break
    n += 1