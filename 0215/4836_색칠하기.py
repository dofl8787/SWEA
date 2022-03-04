import sys
sys.stdin = open('4836.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    count = 0
    for i in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        # count = 0 <- 돌때마다 매번 초기화 시키면 누적 시킨 거 사라지니까 위로 올리기 ^^ 확인하기~~~
        for j in range(r1, r2+1):
            for k in range(c1, c2+1):
                if color == 1:
                    if arr[j][k] == 2:
                        arr[j][k] = 3
                        count += 1
                    else:
                        arr[j][k] = 1
                elif color == 2:
                    if arr[j][k] == 1:
                        arr[j][k] = 3
                        count += 1
                    else:
                        arr[j][k] = 2

    print(f'#{tc+1} {count}')
