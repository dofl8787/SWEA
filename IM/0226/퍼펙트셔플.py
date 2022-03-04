import sys
sys.stdin = open('ps.txt')

T = int(input())
for tc in range(T):
    n = int(input())
    mid = n // 2
    arr = list(input().split())

    a = b = result = []
    c= []
    if n % 2 == 0:
        a = arr[:mid]
        b = arr[mid:]

    if n % 2 == 1:
        a = arr[:mid+1]
        b = arr[mid+1:]

        c.append(a.pop(-1))

    for i in range(mid):
        result.append(a[i])
        result.append(b[i])
    if n % 2 == 1:
        result.append(*c)
    print(f'#{tc+1}', *result)

