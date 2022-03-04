import sys
sys.stdin = open('sdoku.txt')

T = int(input())

for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]

    #행
    result = 1
    for i in range(9):
        num_lst = [0]*10
        for j in range(9):
            num_lst[arr[i][j]] += 1

        for num in range(1,10):
            if num_lst[num] != 1:
                result = 0
                break

    for i in range(9):
        num_lst = [0]*10
        for j in range(9):
            num_lst[arr[j][i]] += 1

        for num in range(1,10):
            if num_lst[num] != 1:
                result = 0
                break

    for n in range(0,7,3):
        for m in range(0,7,3):
            num_lst = [0]*10
            for sn in range(3):
                for sm in range(3):
                    num_lst[arr[n+sn][m+sm]] += 1

            for num in range(1,10):
                if num_lst[arr[n+sn][m+sm]] != 1:
                    result = 0
                    break

    print(f'#{tc+1} {result}')
