import sys
sys.stdin = open('fish.txt')

def special_fish(lst):
    lst.sort()

    for i in range(N):
        fish = (lst[i]//M)*K

        if lst[i] < M or fish - i <= 0:
            return 'Impossible'
    return 'Possible'




T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    p_lst = list(map(int, input().split()))

    print(f'#{tc+1}', special_fish(p_lst))