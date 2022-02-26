import sys
sys.stdin = open('sdoku.txt')

T = int(input())

for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 0
    for i in range(9):
        new_arr = [0]*10
        for j in range(9):
            new_arr[arr[i][j]] += 1
        for num in range(1, 10):
            if new_arr

    for n in range(len(arr)):
        new_arr2 = []
        for m in range(len(arr)):
            new_arr2.append(arr[m][n])
            if arr[m][n] in new_arr:
                result = 0
                break
            else:
                result = 1

    for p in range(0, 7, 3):
        for q in range(0,7,3):
            new_arr3 =[0]*10
            for x in range(3):
                for y in range(3):
                    new_arr3.append(arr[p+x][q+y])
                    if arr[p+x][q+y] in new_arr3:
                        result = 0
                    else:
                        result = 1
        print(result)






