N = int(input())

result = list(map(int, input().split()))

for _ in range(1, N):
    R, G, B = map(int, input().split())
    tmp = result[:]
    result[0] = min(tmp[1], tmp[2]) + R
    result[1] = min(tmp[0], tmp[2]) + G
    result[2] = min(tmp[0], tmp[1]) + B

print(min(result))