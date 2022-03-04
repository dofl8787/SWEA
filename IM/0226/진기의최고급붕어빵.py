import sys
sys.stdin = open('fish.txt')

T = int(input())

for tc in range(T):
    N,M,K = map(int, input().split())
    p_lst = list(map(int, input().split()))
    p_lst.sort()

    cnt = 0
    result = 'Possible'
    for i in range(N):
        fish = (p_lst[i] // M) * K
        cnt += 1
        if p_lst[i] < M:
            result = 'Impossible'
            break


    if fish - cnt <= 0:
        result = 'Impossible'

    print(f'#{tc+1} {result}')
