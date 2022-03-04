import sys
sys.stdin = open('flatten.txt')

count = 0
for tc in range(1, 11):
    N = int(input())
    box_list = list(map(int, input().split()))

    # 0 ~ N-1번까지 총 N번
    for _ in range(N):
        maxnum = minnum = 0
        for num in range(100) :
            if box_list[maxnum] <= box_list[num]:
                maxnum = num
                # print(box_list)
            if box_list[minnum] >= box_list[num]:
                minnum = num
        box_list[maxnum] -= 1
        box_list[minnum] += 1

    count += 1

    maxnum = minnum = 0
    for num in range(100) :
        if box_list[maxnum] <= box_list[num]:
            maxnum = num
            # print(box_list)
        if box_list[minnum] >= box_list[num]:
            minnum = num

    print(f'{box_list[maxnum] - box_list[minnum]}')