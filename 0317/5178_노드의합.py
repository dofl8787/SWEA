import sys
sys.stdin = open('5178.txt')

def postorder(v):
    if v > N: return

    postorder(v * 2)
    postorder(v * 2 + 1)
    arr[v // 2] += arr[v]
    # print(v, arr, end='' )
    # print(v, end='')

T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)

    for i in range(M):
        a,b = map(int, input().split())
        arr[a] = b

    postorder(1)
    print(f'#{tc+1} {arr[L]}')


