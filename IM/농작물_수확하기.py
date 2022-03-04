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
    for m in range(mid+1, n):
        for b in range(n-m+mid-1,m-mid-1,-1):
            result.append(arr[m][b])


    print(f'#{tc+1}',sum(result))

