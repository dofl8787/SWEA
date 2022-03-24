import sys
sys.stdin = open('1240.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]

    hx_lst = {
        '0001101' : 0,
        '0011001' : 1,
        '0010011' : 2,
        '0111101' : 3,
        '0100011' : 4,
        '0110001' : 5,
        '0101111' : 6,
        '0111011' : 7,
        '0110111' : 8,
        '0001011' : 9
    }


    #코드가 시작되는 첫 줄 가져오기
    f_code = ''
    for i in range(N):
        if '1' in arr[i] and len(f_code) == 0:
            f_code += arr[i]
            break

    #코드포함한 줄에서 코드만 가져오기
    start = 0
    barcode = []
    # 맨 끝자리를 찾고, 56자리 저장해주기 (항상 끝은 1)
    # 코드를 돌면서 암호코드 리스트로 받기
    for d in range(M-1,-1,-1):
        if f_code[d] == '1' and start == 0:
            start = d
            for num in range(start-55, start+1, 7):
                code = ''
                for cd in range(num, num+7):
                    code += f_code[cd]
                barcode.append(hx_lst[code])

    num_sum = 0
    result = 0

    for s in range(8):
        if s % 2 == 0:
            result += (barcode[s] * 3)
            num_sum += barcode[s]
        else:
            result += barcode[s]
            num_sum += barcode[s]

    #검증
    if result  % 10 == 0:
        print (f'#{tc+1} {num_sum}')
    else:
        print(f'#{tc+1} {0}')


