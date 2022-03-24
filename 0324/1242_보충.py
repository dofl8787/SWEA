import sys
sys.stdin = open('1242.txt')

def hex(hexV):
    hCode = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
    }
    return hCode[hexV]

sCode = {211:0, 221:1, 122:2, 411:3, 132:4, 231:5, 114:6, 312:7 , 213:8, 112:9}

T =int(input())
for tc in range(T):
    N,M = map(int, input().split())
    arr = [input() for _ in range(N)]

    arr2 = [''for _ in range(N)]

    for i in range(N):
        for j in range(M):
            arr2[i] += hex(arr[i][j])

    result = 0
    #상단의 우측부터 코드의 끝지점을 찾아보자.
    for y in range(1, N):
        x = M*4 -1
        while x > 0:
            numbers = ['-'] * 8
            if arr2[y][x] == '1' and arr2[y-1][x] == '0':
                for k in range(7, -1, -1):

                #코드의 오른쪽 끝을 찾은 것
                #오른쪽 끝의 1의 갯수
                    cnt1 = 0
                    while arr2[y][x] == '1':
                        cnt1 += 1
                        x -= 1

                    # 0의 갯수
                    cnt2 = 0
                    while arr2[y][x] == '0':
                        cnt2 += 1
                        x -= 1
                    # 다음 1의 갯수
                    cnt3 = 0
                    while arr2[y][x] == '1':
                        cnt3 += 1
                        x -= 1

                    #0만큼 앞으로 이동
                    while arr2[y][x] == '0':
                        x -= 1

                    #비율(두께)를 찾는다.
                    l = min(cnt1, cnt2, cnt3)
                    numbers[k] = sCode[cnt3//l*100 + cnt2//l*10 + cnt1//l]

                odd_sum = numbers[0] + numbers[2] + numbers[4] + numbers[6]
                even_sum = numbers[1] + numbers[3] + numbers[5]
                if (odd_sum*3 + even_sum + numbers[7]) % 10 == 0:
                    result += sum(numbers)
            else:
                x -= 1

    print(f'#{tc+1} {result}')
