def solution(key, lock):
    M = len(key)
    N = len(lock)
    
    LOCK = [[0] * 60 for _ in range(60)]
    for i in range(N):
        for j in range(N):
            LOCK[i + N][j + N] = lock[i][j]
        
    for _ in range(4):
        for Li in range(N * 2):
            for Lj in range(N * 2):
                
                for Ki in range(M):
                    for Kj in range(M):
                        LOCK[Li + Ki][Lj + Kj] += key[Ki][Kj]
                
                flag = 0
                for i in range(N):
                    for j in range(N):
                        if LOCK[i + N][j + N] != 1:
                            flag = 1
                if not flag:
                    return True
                
                for Ki in range(M):
                    for Kj in range(M):
                        LOCK[Li + Ki][Lj + Kj] -= key[Ki][Kj]
        key = list(map(list, zip(*key[::-1])))
    return False