import sys
sys.stdin = open('a.txt')

T = int(input())

for tc in range(T):
    n = int(input())

    arr = [list(input()) for _ in range(n)]

    ud = [-1, 1, 0, 0]
    rl = [0, 0, 1, -1]

    for i in range(n):
        for j in range(n):
                if arr[i][j] == 'A':
                    for d in range(4):
                        nr = i+ud[d]
                        nc = j+rl[d]
                        if 0 <= nc < n and 0 <= nr < n:
                            if arr[nc][nr] == 'H':
                                arr[nc][nr] = 'X'
                elif arr[i][j] == 'B':
                    for d in range(4):
                        nr = i+ud[d]
                        nc = j+rl[d]
                        cnt = 0
                        while 0 <= nr < n and 0 <= nc < n and cnt < 2:
                            if arr[nr][nc] == 'H':
                                arr[nr][nc] = 'X'
                            nr, nc = nr + ud[d], nc + rl[d]
                            cnt += 1
                elif arr[i][j] == 'C':
                    for d in range(4):
                        nr = i + ud[d]
                        nc = j + rl[d]
                        cnt = 0
                        while 0 <= nr < n and 0 <= nc < n and cnt < 3:
                            if arr[nr][nc] == 'H':
                                arr[nr][nc] = 'X'
                            nr, nc = nr + ud[d], nc + rl[d] #줄 붙여넣기 잘하기 ^^ ..
                            cnt += 1

    result = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 'H':
                result += 1
    print(result)