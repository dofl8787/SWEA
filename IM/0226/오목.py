import sys
sys.stdin = open('omok.txt')


def omok(arr):

    ud = [0,1,1,1]#우하좌대우대
    rl = [1,0,-1,1]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for d in range(4):
                    nr, nc = i, j
                    cnt = 0
                    while 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 'o':
                        cnt += 1
                        nr += ud[d]
                        nc += rl[d]

                        if cnt == 5:
                            return 'YES'

    return 'NO'


T = int(input())
for tc in range(T):
    n = int(input())
    omok_lst = [list(input()) for _ in range(n)]

    print(f'#{tc+1}', omok(omok_lst))
