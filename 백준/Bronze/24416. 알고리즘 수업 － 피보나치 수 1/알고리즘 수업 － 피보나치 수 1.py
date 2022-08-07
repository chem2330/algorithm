def fib(n):
    global fib_cnt
    if n == 1 or n == 2:
        return 1
    fib_cnt += 1
    return fib(n - 1) + fib(n - 2)


n = int(input())
fib_cnt = 0
fib(n)
print(fib_cnt + 1)
print(n - 2)