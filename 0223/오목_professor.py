import sys
sys.stdin = open('b.txt')


# 행 우선순회를 하다가 'o'가 나오면 오른쪽, 아래쪽, 우하단, 좌하단으로 검사
# 5개를 찾으면 빠져나와야 하기 때문에 함수로 만드는게 편함
def solve(arr):

    dr = [0, 1, 1, 1] #우, 하, 우하단, 좌하단
    dc = [1, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(4):
                    r,c = i,j #현재 위치 저장, 반복문을 돌 때마다 현재 위치 기준으로 시작해야 함
                    #해당 방향으로 계속 이동하면서 개수 세기
                    # r,c가 범위 안에 있으면서 돌이 놓여 있으면 , 계속 반복하며 개수 세기
                    cnt = 0 #연속적으로 놓여져 있는 돌을 세기 위한 변수
                    while 0<= r < N and 0 <= c < N and arr[r][c] == 'o':
                        cnt += 1
                        r += dr[d]
                        c += dc[d]
                        if cnt >= 5:
                            return 'YES'
    return('NO') #for를 다 돌았는데 못찾을 경우




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    print(solve(arr))
