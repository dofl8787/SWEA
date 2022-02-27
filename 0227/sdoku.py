import sys
sys.stdin = open('sdoku.txt')

def sdoku(lst):
    for i in range(9):
        new_arr = [0]*10
        for j in range(9):
            new_arr[lst[i][j]] += 1

        for num in range(1, 10):
            if new_arr[num] != 1:
                return 0

    for i in range(9):
        new_arr = [0]*10
        for j in range(9):
            new_arr[lst[j][i]] += 1

        for num in range(1, 10):
            if new_arr[num] != 1:
                return 0

    for n in range(0,7,3):
        for m in range(0,7,3):
            new_arr2 =[0]*10
            for sn in range(3):
                for sm in range(3):
                    new_arr2[lst[n+sn][m+sm]] += 1

        for nums in range(1,10):
            if new_arr2[nums] != 1:
                return 0
    return 1



T = int(input())

for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{tc+1}', sdoku(arr))