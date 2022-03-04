import sys
sys.stdin = open('memory.txt')

T = int(input())

for tc in range(T):
    text = list(map(int, input()))
    N = len(text)
    new_arr =[0] * N
    cnt = 0
    for i in range(N):
        if text[i] != new_arr[i]:
            for j in range(i,N):
                new_arr[j] = text[i]
            cnt += 1

    print(f'#{tc+1} {cnt}')