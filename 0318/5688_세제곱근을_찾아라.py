import sys
sys.stdin = open('5688.txt')

T= int(input())
for tc in range(T):
    N = int(input())

    num = N ** (1.0/3.0)
    print(num)
    if num == int(num):
        print(f'#{tc+1} {int(num)}')
    else:
        print(f'#{tc+1} {-1}')