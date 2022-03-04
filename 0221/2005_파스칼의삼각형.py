import sys
sys.stdin = open('a.txt')

T = int(input())
for tc in range(T):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    print(f'#{tc+1}')

    for r in range(N):
        for c in range(N):
            if c == 0 or r == c:
                arr[r][c] = 1
            else:
                arr[r][c] = arr[r - 1][c - 1] + arr[r - 1][c]

            if arr[r][c] != 0:
                print(arr[r][c], end=' ')
        print()