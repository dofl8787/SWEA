import sys
sys.stdin = open('harvesting.txt')
T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    mid = n //2

    result = []


    for j in range(mid+1):
        for k in range(mid-j, mid+j+1):
            result.append(arr[j][k])
    for a in range(mid+1, n):
        for b in range(a-mid, n-a+mid):
            result.append(arr[a][b])


    print(f'#{tc+1}',sum(result))


