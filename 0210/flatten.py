import sys
sys.stdin = open('flatten.txt')

for tc in range(1, 11):
    N = int(input())
    box_list = list(map(int, input().split()))

    for i in range(N):
        max = min = 0
        for num in range(len(box_list)):
            if box_list[max] <= box_list[num]:
                max = num
            if box_list[min] >= box_list[num]:
                min = num

        box_list[max] -= 1
        box_list[min] += 1


    for num in range(100) :
        if box_list[max] <= box_list[num]:
            max = num
            # print(box_list)
        if box_list[min] >= box_list[num]:
            min = num



    # print(f'max : {box_list[max]}, min : {box_list[min]}')
    # print(max, min)
    print(f'#{tc} {box_list[max]-box_list[min]}')
# max값에서 min한테 1을 빼주기
# max -= 1
# min += 1
# for i in range (N)

#다 돌리고 난 애들 사이에서 max min 구하고 -

#위치를 구해서 값을 구해야지
#idx를 찾기