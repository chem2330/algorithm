nine = []
for _ in range(9):
    nine.append(int(input()))

for i in range(8, 0, -1):
    for j in range(0, i):
        if nine[j] > nine[j + 1]:
            nine[j], nine[j + 1] = nine[j + 1], nine[j]

cnt = 0
for k1 in range(8):
    for k2 in range(k1 + 1, 9):
        counts = [1] * 9
        counts[k1] = 0
        counts[k2] = 0

        if cnt == 1:
            break

        heigh_sum = 0
        heights = []
        for idx in range(9):
            if counts[idx] == 1:
                heigh_sum += nine[idx]
                heights.append(nine[idx])

        if heigh_sum == 100:
            cnt = 1
            for index in range(7):
                print(heights[index])