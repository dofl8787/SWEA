import sys
sys.stdin = open('omok.txt')


def omok(arr):
    ud = [0, 1, 1, 1] #우, 하, 우하단, 좌하단
    rl = [1, 0, 1, -1]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for d in range(4):
                    nr = i + ud[d]
                    nc = j + rl[d]
                    cnt = 1 #이미 o를 한 번 찾았으니까  cnt = 1로 설정
                    #만약 cnt를 다 찾고 싶으면 nr ,nc = i, j로 설정정                    while 0<= nr < n and 0 <= nc < n and arr[nr][nc] =='o':
                        cnt += 1
                        nr = nr + ud[d]
                        nc = nc + rl[d]


                        if cnt >= 5:
                            return 'YES'
    else:
        return 'No'
T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    print(omok(arr))