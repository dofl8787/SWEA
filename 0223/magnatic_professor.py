import sys
sys.stdin = open('a.txt')


T = 10
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    result = 0 #교착상태를 더해줄 최종값
    prev = [0]*N
    # 내 위쪽에 있는 자석이 어떤 녀석인지 저장하는 배열 = prev / 구냥 []해도 ㄱㅊ을듯
    for i in range(N):
        for j in range(N):
            # if table[i][j] == 0: #아무것도 아니기 때문에 생각할 필요 없음
            #     pass
            if table[i][j] == 1: #N극인 경우
                prev[j] = 1
            elif table[i][j] == 2:  #S극인 경우
                if prev[j] == 1: #교착 상태
                    result += 1
                prev[j] = 2

    print(f'#{tc} {result}')