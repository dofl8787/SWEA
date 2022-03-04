import sys
sys.stdin = open('4843.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    aj = list(map(int, input().split()))

    for i in range(N-1):
        if i % 2 == 1:
            min_num = i
            for j in range(i+1, N):
                if aj[min_num] > aj[j]:
                    min_num = j
            aj[i], aj[min_num] = aj[min_num], aj[i]
        else:
            max_num = i
            for j in range(i+1, N):
                if aj[max_num] < aj[j]:
                    max_num = j
            aj[i], aj[max_num] = aj[max_num], aj[i]
    print(f'#{tc+1}',*aj[:10])

