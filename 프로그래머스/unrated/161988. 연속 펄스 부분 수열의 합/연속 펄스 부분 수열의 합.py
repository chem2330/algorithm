def solution(sequence):
    answer = 0
    new_seq = []
    for i in range(len(sequence)):
        if i % 2:
            new_seq.append(-sequence[i])
        else:
            new_seq.append(sequence[i])

    dp = [[0, 0] for _ in range(len(sequence))]  # [min, max]
    dp[0] = [new_seq[0], new_seq[0]]

    for i in range(1, len(sequence)) :
        num = new_seq[i]
        dp[i][0] = min(num, num + dp[i-1][0])
        dp[i][1] = max(num, num + dp[i-1][1])
    # print(dp)
    mmin = min(map(min, dp))
    mmax = max(map(max, dp))
    # print(mmin, mmax)
    return max(-mmin, mmax)