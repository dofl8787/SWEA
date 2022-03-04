import sys
sys.stdin = open('4837.txt')
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    a = len(A)

    num = 0
    for i in range(1 << a):
        num_sum = a_lst = count = 0
        for j in range(a):
            if i & (1 << j):
                a_lst = A[j]
                num_sum += a_lst
                count += 1

        if count == N and num_sum == K:
            num += 1
    print (f'#{tc+1} {num}')
