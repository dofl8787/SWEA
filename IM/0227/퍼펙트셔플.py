import sys
sys.stdin = open('ps.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = input().split()

    mid = N//2
    arr3 =''
    if N % 2 == 0 : #짝수
        arr1 = arr[:mid]
        arr2 = arr[mid:]
    else:
        arr1 = arr[:mid+1]
        arr2 = arr[mid+1:]
        arr3 = arr1.pop(-1)

    result = []
    for i in range(mid):
        result.append(arr1[i])
        result.append(arr2[i])
    if N % 2 == 1:
        result.append(arr3)

    print(f'#{tc+1}', *result)
