import sys
sys.stdin = open('haek.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    #

    ud = [-1,1,0,0]
    rl = [0,0,-1,1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                for d in range(4):
                    nr = i+rl[d]
                    nc = j+ud[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        arr[nr][nc] = 'X'
            elif arr[i][j] == 'B':
                for d in range(4):
                    nr = i + rl[d]
                    nc = j + ud[d]
                    cnt = 0
                    while 0 <= nr < N and 0 <= nc < N and cnt < 2:
                        if arr[nr][nc] == 'H':
                            arr[nr][nc] = 'X'
                        nr += rl[d]
                        nc += ud[d]
                        cnt += 1
            elif arr[i][j] == 'C':
                for d in range(4):
                    nr = i + rl[d]
                    nc = j + ud[d]
                    cnt = 0
                    while 0 <= nr < N and 0 <= nc < N and cnt < 3:
                        if arr[nr][nc] == 'H':
                            arr[nr][nc] = 'X'
                        nr += rl[d]
                        nc += ud[d]
                        cnt += 1


    result = 0
    for k in range(N):
        for m in range(N):
            if arr[k][m] == 'H':
                result += 1

    print(result)