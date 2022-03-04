import sys
sys.stdin = open('1989.txt')


T = int(input())

for tc in range(T):
    A = list(input())
    a = len(A)
    b = 0
    for i in range(a//2):
        if A[i] == A[a-1-i]:
            b = 1
        else:
            b
    print(f'#{tc+1} {b}')

