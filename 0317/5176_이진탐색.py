import sys
sys.stdin = open('5176.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [0] * (N+1)
    cnt = 1

    def inorder(v):
        global cnt
        if v > N:return
        inorder(v * 2)
        arr[v] = cnt
        cnt += 1
        inorder(v * 2 + 1)

    inorder(1)

    print(f'#{tc+1} {arr[1]} {arr[N//2]}')
    # for i in range(len(arr)):
    #     if i == 1:
    #         print(arr[i], end=' ')
    #     if i == N//2:
    #         print(arr[i])
