import sys
sys.stdin = open('6359.txt')
T = int(input())


for _ in range(T):
    n = int(input())
    arr = [0] * (n+1)
    for k in range(1, n+1):
        num = n // k
        for i in range(1, num+1):
            if arr[i*k] == 0:
                arr[i*k] = 1
            elif arr[i*k] == 1:
                arr[i*k] = 0

    cnt = 0
    for j in range(len(arr)):
        if arr[j] == 1:
            cnt += 1
    print(cnt)

