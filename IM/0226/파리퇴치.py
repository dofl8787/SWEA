import sys
sys.stdin = open('pary.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mx_num = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            num_sum = 0
            for si in range(M):
                for sj in range(M):
                    num_sum += arr[i+si][j+sj]


            if mx_num < num_sum:
                mx_num = num_sum

    print(f'#{tc+1} {mx_num}')




