import sys
sys.stdin = open('12919.txt')

T = int(input())
for tc in range(T):

    N = float(input())

    result = ''


    x = 1
    for _ in range(13):
        x = N*2
        if x >= 1:
            N = x - 1
            result += '1'
        elif 0 < x < 1 :
            result += '0'
            N *= 2


    if N != 0:
        print(f'#{tc+1} overflow')
    else:
        print(f'#{tc+1} {result}')
# while N > 0:
#