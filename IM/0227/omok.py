import sys
sys.stdin = open('omok.txt')



def omok(lst):

    ud = [0, 1, 1, 1]
    rl = [1, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if lst[i][j] == 'o':
                for d in range(4):
                    nr = i + ud[d]
                    nc = j + rl[d]
                    cnt = 1
                    while 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == 'o':
                        cnt += 1
                        nr += ud[d]
                        nc += rl[d]

                        if cnt == 5:
                            return 'YES'

    return'NO'













T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]


    print(f'#{tc+1}', omok(arr))