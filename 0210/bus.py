import sys
sys.stdin = open('bus.txt')

for tc in range(int(input())):
    K, N, M  = map(int, input().split())
    stop = list(map(int, input().split()))

    cur = 0
    count = 0

    while cur + K < N:
        for i in range(cur + K, cur, -1):
            if i in stop:
                cur = i
                count += 1
                break
        else: #for - else문 돌거임
            count = 0
            break

    print(f'#{tc+1} {count}')