import sys
sys.stdin = open('4869.txt')

def p_paper(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    else:
        return p_paper(n-10) + p_paper(n-20)*2

T = int(input())
for tc in range(T):
    n = int(input())
    print(f'#{tc+1} {p_paper(n)}')