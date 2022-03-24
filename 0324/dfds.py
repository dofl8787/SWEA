import sys
sys.stdin = open('1242.txt')

def hextobin(hexV):
    hCode = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    return hCode[hexV]

sCode = {211:0 , 221:1, 122:2, 411:3, 132:4, 231:5, 114:6, 312:7, 213:8, 112:9}

T = int(input())
#T = 1
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    arr2 = ['' for _ in range(N)]
    #print(arr)

    for i in range(N):
        for j in range(M):
            arr2[i] += hextobin(arr[i][j])

    #print(arr2)
    # 상단의 우측부터 코드의 끝지점을 찾아보자
    result = 0
    for y in range(1, N):
        x = M*4-1
        while x > 0:
            numbers = ['-'] * 8
            if arr2[y][x] == '1' and arr2[y-1][x] == '0':
                for i in range(7, -1, -1):
                    # 코드의 오른쪽 끝을 찾은 것
                    # 오른쪽 끝의 1의 개수
                    cnt1 = 0
                    while arr2[y][x] == '1':
                        cnt1 += 1
                        x -= 1
                    # 다음 0의 개수
                    cnt2 = 0
                    while arr2[y][x] == '0':
                        cnt2 += 1
                        x -= 1

                    # 다음 1의 개수
                    cnt3 = 0
                    while arr2[y][x] == '1':
                        cnt3 += 1
                        x -= 1

                    # 0만큼 앞으로 이동
                    while arr2[y][x] == '0':
                        x-= 1

                    # 두께 찾는다.
                    k = min(cnt1, cnt2, cnt3)
                    numbers[i] = sCode[cnt3//k*100 + cnt2//k*10 + cnt1//k]
                #print(numbers)
                oddsum = numbers[0] + numbers[2] + numbers[4] + numbers[6]
                evensum = numbers[1] + numbers[3] + numbers[5]
                if (oddsum*3 + evensum + numbers[7]) % 10 == 0:
                    result += sum(numbers)
            else:
                x -= 1

    print(f'#{tc} {result}')