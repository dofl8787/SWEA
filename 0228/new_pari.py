import sys
sys.stdin = open('new_pari.txt')

T = int(input())

for tc in range(T):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ud = [1, -1, 0, 0]  # 하상우좌
    rl = [0, 0, 1, -1]

    sr = [-1, 1, 1, -1]
    sc = [1, 1, -1, -1]


    mx_num = 0
    for i in range(N):
        for j in range(N):
            num_sum = arr[i][j]
            for d in range(4):
                nr = i + rl[d]
                nc = j + ud[d]
                cnt = 1
                while 0 <= nr < N and 0 <= nc < N and cnt < M:
                    num_sum += arr[nr][nc]
                    nr , nc = nr+rl[d], nc+ud[d]
                    cnt += 1
            if mx_num < num_sum:
                mx_num = num_sum


    for r in range(N):
        for c in range(N):
            num_sum2 = arr[r][c]
            for dd in range(4):
                nrr = r + sr[dd]
                ncc = c + sc[dd]
                cnt = 1
                while 0 <= nrr < N and 0 <= ncc < N and cnt < M:
                    num_sum2 += arr[nrr][ncc]
                    nrr, ncc = nrr+sr[dd],  ncc + sc[dd]
                    cnt += 1
            if mx_num < num_sum2:
                mx_num = num_sum2

    print(f'#{tc+1} {mx_num}')



#상하




#대각