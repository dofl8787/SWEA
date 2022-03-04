import sys
sys.stdin = open('4865.txt')

T = int(input())

for tc in range(T):
    str1 = list(input())
    str2 = list(input())
    N = len(str1)
    M = len(str2)

    bucket = [0]*N
    for i in range(M):
        for j in range(N):
            if str1[j] == str2[i]:
                bucket[j] += 1
    mx_num = 0
    for k in bucket:
        if mx_num <= k:
            mx_num = k

    print(f'#{tc+1} {mx_num}')