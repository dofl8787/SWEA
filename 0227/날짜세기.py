import sys
sys.stdin = open('daycount.txt')

T = int (input())

day ={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for tc in range(T):
    m1, d1, m2, d2 = map(int, input().split())

    day_cnt = 0
    if m1 == m2:
        day_cnt = d2 - d1 + 1
        print(f'#{tc+1} {day_cnt}')
    else:

        for i in range(m1, m2+1):
            if i == m1:
                day_cnt += day[i] - d1 + 1
            elif i == m2:
                day_cnt += d2
            else:
                day_cnt += day[i]



        print(f'#{tc+1} {day_cnt}')


