import sys
sys.stdin = open('bus.txt')

for tc in range(int(input())):
    K, N, M = map(int, input().split())
    stop = list(map(int, input().split()))

    cur = 0  # 전기버스의 현재 위치
    cnt = 0  # 충전횟수

    while cur + K < N:
        for i in range(cur + K, cur, -1):
            if i in stop:
                cur = i  # 충전하기
                cnt += 1
                break
        else:
            cnt = 0
            break
    print(cnt)
