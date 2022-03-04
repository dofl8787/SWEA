import sys
sys.stdin = open('1206.txt')


import sys
sys.stdin = open('1206.txt')

for tc in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))
    result = 0

    #for i in T : T를 돌 때
    for i in range(2, T-2):

    # 만약 i-2, i-1, i, i+1, i+2 중 i가 가장 클 때,
        if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i+1] < arr[i] and arr[i+2] < arr[i]:
            #i-2 ~ i+2 중 가장 큰 수를 찾고. arr[i]에서 빼기
            numbers = [arr[i-2],arr[i-1],arr[i+1],arr[i+2]]
            max_num = numbers[0]
            for number in numbers:
                if max_num < number:
                    max_num = number

            result += (arr[i]-max_num)
    print(f"#{tc} {result}")













    # print(f"#{tc} {ans}")
    # print('#{} {}'.format(tc, ans))
    # print(arr)
