import sys
sys.stdin = open('number_card.txt')

T = int(input()) #전체 케이스 개수

for m in range(T):
    N = int(input()) #카드 장수
    ai = list(map(int, input())) #원본 자료
    max_num = ai[0]
    for j in range(N):
        if max_num < ai[j]:
            max_num = ai[j]
    C = [0]*(max_num + 1) #카운팅

    for val in ai:
        C[val] += 1

    max = C[0]
    idx = 0
    for i in range(len(C)):
        if max <= C[i]:
            max = C[i]
            idx = i
    print(f'#{m+1} {idx} {max}')

    # string = '123456'
    #
    # arr = list(string)
    # cnt - [0] * 10(0
    # ~9)
    # for num in arr:
    #     cnt[int(num)] += 1
    #
    # arr = list(map(int, string))  # string은 input으로 받으면 됨
    # print(arr)
