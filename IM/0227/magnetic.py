import sys
sys.stdin = open('magnetic.txt')

for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            elif arr[j][i] == 2:
                if cnt != 0:
                    result += 1
                cnt = 0

    print(f'#{tc+1} {result}')
