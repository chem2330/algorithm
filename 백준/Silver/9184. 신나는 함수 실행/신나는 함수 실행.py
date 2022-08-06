import sys


input = sys.stdin.readline

def w(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    elif x > 20 or y > 20 or z > 20:
        return 2 ** 20
    elif arr[x][y][z]:
        return arr[x][y][z]
    elif x < y and y < z:
        arr[x][y][z] = w(x, y, z - 1) + w(x, y - 1, z - 1) - w(x, y - 1, z)
        return arr[x][y][z]
    else:
        arr[x][y][z] = w(x - 1, y, z) + w(x - 1, y - 1, z) + w(x - 1, y, z - 1) - w(x - 1, y - 1, z - 1)
        return arr[x][y][z]

arr = [[[0] * 21 for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = ', end='')
    print(w(a, b, c))