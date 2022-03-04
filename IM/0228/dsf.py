import sys
sys.stdin = open('bus.txt')


T = int(input())
for tc in range(1, T + 1):
    station = [0] * 1001
    N = int(input())
    for _ in range(N):
        bus, A, B = map(int, input().split())
        if bus == 1:
            for k in range(A, B + 1):
                station[k] += 1
        elif bus == 2:
            for k in range(A, B, 2):
                station[k] += 1
            station[B] += 1
        else:
            if A & 1:
                for k in range(A + 1, B):
                    if k % 10 != 0 and k % 3 == 0:
                        station[k] += 1
                station[A] += 1
                station[B] += 1
            else:
                for k in range(A + 1, B):
                    if k % 4 == 0:
                        station[k] += 1
                station[A] += 1
                station[B] += 1

            print(station)
    # max_station = 0
    # for i in range(1, 1001):
    #     if max_station < station[i]:
    #         max_station = station[i]
    # print(f'#{tc} {max_station}')