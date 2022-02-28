import sys
sys.stdin = open('bus.txt')

T = int(input())
for tc in range(T):
    n = int(input())
    busstop = [0]*1001
    for _ in range(n):
        bus, stop1, stop2 = map(int, input().split())


        if bus == 1:
            for i in range(stop1, stop2 + 1):
                busstop[i] += 1

        elif bus == 2:
            if stop1 % 2 == 1:
                for j in range(stop1, stop2, 2):
                    busstop[j] += 1
                busstop[stop2] += 1
            elif stop1 % 2 == 0:
                for k in range(stop1, stop2, 2):
                    busstop[k] += 1
                busstop[stop2] += 1

        elif bus == 3:

            if stop1 % 2 == 1:
                for m in range(stop1+1,stop2):
                    if m % 3 == 0 and m % 10 != 0:
                        busstop[m] += 1
                busstop[stop1] += 1
                busstop[stop2] += 1
            else:
                for b in range(stop1+1, stop2):
                    if b % 4 == 0:
                        busstop[b] += 1
                busstop[stop1] += 1
                busstop[stop2] += 1


        mx_stop = 0
        for num in busstop:
            if mx_stop < num:
                mx_stop = num
    print(f'#{tc+1} {mx_stop}')


