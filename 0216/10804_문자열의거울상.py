import sys
sys.stdin = open('10804.txt')

T = int(input())

for tc in range(T):
    A = list(input())
    a = len(A)
    b = ''
    for i in range(a//2):
        A[i], A[a - 1 -i] = A[a - 1 - i], A[i]
    for j in range(a):
        if A[j] == 'd':
            A[j] = 'b'
        elif A[j] == 'b':
            A[j] = 'd'
        elif A[j] == 'q':
            A[j] = 'p'
        elif A[j] == 'p':
            A[j] = 'q'
    print(f'#{tc+1} {"".join(A)}')