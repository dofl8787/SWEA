# delta

arr = [['-'] * 5 for _ in range(5)]

# r, c의 상하 좌우 위치
r = c = 2                   # 기준점
arr[r][c] = '#'
arr[r - 1][c + 0] = '*'     # 상
arr[r + 1][c + 0] = '*'     # 하
arr[r + 0][c - 1] = '*'     # 좌
arr[r + 0][c + 1] = '*'     # 우

for lst in arr:
    print(*lst)
#====================================================
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
r = c = 2
for i in range(4):  # 네방향의 좌표를 생성
    tr = r + dr[i]
    tc = c + dc[i]
    arr[tr][tc] = i + 1

for lst in arr:
    print(*lst)

#====================================================
from random import randint
N = 5
arr = [[randint(1, 6) for _ in range(N)] for _ in range(N)]

# 모든 위치에서 네 방향 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(N):
    for c in range(N):
        # r, c
        for i in range(4):  # 네방향의 좌표를 생성
            # (r, c) + dr, dc 를 생성
            nr = r + dr[i]
            nc = c + dc[i]
            # 인덱스 범위 내의 값인지 체크
            if 0 <= nr < 5 and 0 <= nc < 5:
                arr[nr][nc]

for lst in arr:
    print(*lst)
