dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, 1, -1]

N, K = 9, 4
arr = [[' '] * N for _ in range(N)]
r, c = 3, 7

for i in range(4):
    nr, nc = r, c
    cnt = 0
    while 0 <= nr + dr[i] < N and 0 <= nc + dc[i] < N and cnt < K:
        nr, nc = nr + dr[i], nc + dc[i]
        arr[nr][nc] = i + 1
        cnt += 1


for lst in arr:
    print(*lst)
print('---------------------')

# ===========================================
# delta 를 적용해서 변경하고 범위 체크

dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, 1, -1]

N, K = 9, 4
arr = [[' '] * N for _ in range(N)]
r, c = 6, 6

for i in range(4):
    nr, nc = r + dr[i], c + dc[i]           # while 전에 한 칸 전진
    cnt = 0
    while 0 <= nr < N and 0 <= nc < N and cnt < K:
        arr[nr][nc] = i + 1
        nr, nc = nr + dr[i], nc + dc[i]
        cnt += 1

for lst in arr:
    print(*lst)
print('---------------------')

# ===========================================
# while이 싫어요!!!! 죽어도 for 못 잊어...

N = 9
arr = [[' '] * N for _ in range(N)]
r, c = 6, 6

for i in range(4):
    nr, nc = r, c
    for j in range(K): # 상
        nr, nc = nr + dr[i], nc + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N: break
        arr[nr][nc] = i + 1

for lst in arr:
    print(*lst)

