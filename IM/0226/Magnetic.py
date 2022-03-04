import sys
sys.stdin = open('Magnetic.txt')

for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for j in range(N):
        new_arr = []
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                new_arr.append(arr[i][j])
            elif arr[i][j] == 2 and new_arr:
                cnt += 1
                new_arr=[]


        result += cnt
    print(f'#{tc+1} {result}')

