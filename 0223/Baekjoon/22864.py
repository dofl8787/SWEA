A, B, C, M = map(int, input().split())

stress = work = hour = 0

if A > M:
    print(0)

else:
    while hour <= 24:
        if stress + A < M :
            stress += A
            work += B
            hour += 1
        else:
            stress -= C
            hour += 1
            if stress-C < 0:
                stress = 0
    print(work)