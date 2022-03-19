import sys
sys.stdin = open('5174.txt')

T = int(input())
for tc in range(T):
    cnt = 0
    E,N = map(int, input().split())
    arr = list(map(int, input().split()))
    L = [0] * (E+2)
    R = [0] * (E+2)
    for i in range(0, (E*2), 2):
        p = arr[i]
        if L[p] == 0:
            L[p] = arr[i+1]
        else:
            R[p] = arr[i+1]

    def inorder(v):
        global cnt
        if v == 0:
            return

        cnt += 1
        inorder(L[v])
        inorder(R[v])

    inorder(N)
    print(f'#{tc+1} {cnt}')

    # print(lst)
    # print(L,R)
    # print(arr[i], end=' ')
    # print(arr[i+1])
