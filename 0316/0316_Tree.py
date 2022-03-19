import sys
sys.stdin = open('0316.txt')

def inorder(root):
    if int(TREE[root][1]):
        inorder(int(TREE[root][1]))
    print(TREE[root][0], end='')
    if int(TREE[root][2]):
        inorder(int(TREE[root][2]))


for tc in range(10):
    N = int(input())
    TREE = [[0]*3 for _ in range(N+1)]
    for i in range(N):
        arr = list(input().split())
        P = int(arr[0])
        TREE[P][0:len(arr)-1] = arr[1:len(arr)]

    print(f'#{tc+1} ', end='')
    inorder(1)
    print()

    # TREE[P][0] = arr[1]
    # TREE[P][1] = arr[2]
    # if arr[3]:
    #     TREE[P][2] = arr[3]