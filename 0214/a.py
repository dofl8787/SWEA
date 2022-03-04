import sys
sys.stdin = open('a.txt')
#이중 리스트 받기
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
# r은 행, c는 열
    max_num = mx_i = mx_j = 0
    for i in range(N):
        for j in range(N):
            num_sum = 0
            for di, dj in[(0,1), (1,0), (0,-1), (-1,0)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    num_sum += arr[ni][nj]

            if max_num < num_sum:
                max_num = num_sum
                mx_i = i
                mx_j = j

    print(f'#{tc+1} {mx_i} {mx_j} {max_num}')







