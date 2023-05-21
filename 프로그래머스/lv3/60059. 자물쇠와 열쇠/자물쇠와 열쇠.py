def spin_right(arr):
    return list(map(list, zip(*arr[::-1])))

def spin_left(arr):
    return list(map(list, zip(*arr))[::-1])

def check(arr, N):
    answer = True
    for ix in range(N):
        for iy in range(N):
            if arr[ix + N][iy + N] != 1:
                return False
    return answer

def solution(key, lock):
    M = len(key)
    N = len(lock)
    # 3배 더 큰 자물쇠 생성
    new_lock = [[1] * N * 3 for _ in range(N * 3)]
    # 기존 자물쇠를 새로운 자물쇠 가운데에 위치
    for ix in range(N):
        for iy in range(N):
            new_lock[ix + N][iy + N] = lock[ix][iy]
    # 시계방향으로 4번 돌림
    for _ in range(4):
        key = spin_right(key)
        for lock_ix in range(N * 2):
            for lock_iy in range(N * 2):
                # key를 new_lock에 꽂음
                for key_ix in range(M):
                    for key_iy in range(M):
                        new_lock[lock_ix + key_ix][lock_iy + key_iy] += key[key_ix][key_iy]
                # new_lock의 중앙만 확인
                if check(new_lock, N):
                    return True
                # key를 new_lock에서 뺌
                for key_ix in range(M):
                    for key_iy in range(M):
                        new_lock[lock_ix + key_ix][lock_iy + key_iy] -= key[key_ix][key_iy]
    return False