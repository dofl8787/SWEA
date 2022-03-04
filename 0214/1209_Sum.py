import sys
sys.stdin = open('1209.txt')



for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_num = 0

    for i in range(100):
        new_arr = 0
        for j in range(100):
            new_arr += arr[i][j]
        if max_num < new_arr:
            max_num = new_arr

    for m in range(100):
        new_sum = 0
        for n in range(100):
            new_sum += arr[n][m]
        if max_num < new_sum:
            max_num = new_sum


    new_l = 0
    for l in range(100):
        new_l += arr[l][l]
        if max_num < new_l:
            max_num = new_l

    new_o = 0
    for o in range(100):
        new_o += arr[o][99-o]
        if max_num < new_o:
            max_num = new_o

    print(f'#{tc+1} {max_num}')