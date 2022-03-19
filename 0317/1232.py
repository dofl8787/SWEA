import sys
sys.stdin = open('1232.txt')

def postorder(v):
    if v == 0:
        # print(result)
        return
    postorder(L[v])
    postorder(R[v])
    result.append(lst[v])

for tc in range(10):
    N = int(input())

    result = []
    lst = [0]
    R = [0] * (N + 1)
    L = [0] * (N + 1)
    for _ in range(N):
        arr = list(input().split())
        lst.append(arr[1])
        if len(arr) == 4:
            L[int(arr[0])] = int(arr[2])
            R[int(arr[0])] = int(arr[3])
    postorder(1)

    op = ['-', '*', '+', '/']
    total = []
    for j in result:
        if j not in op:
            j = int(j)
            total.append(j)
        else:
            # 빈리스트가 아니면?
            if len(total) > 1:
                b = total.pop()
                a = total.pop()
                if j == '-':
                    total.append(a-b)
                elif j == '+':
                    total.append(a+b)
                elif j == '*':
                    total.append(a*b)
                elif j == '/':
                    total.append(a/b)
    # print(result)
    print(f'#{tc+1}', int(*total))
