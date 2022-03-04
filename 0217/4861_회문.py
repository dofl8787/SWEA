import sys
sys.stdin = open('4861.txt')

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
# 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.
#
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split()) #NxN M은 글자수
#     a = [input() for _ in range(N)]
#     p = ''
#     for i in range(N):
#         for j in range(N-M+1):
#             for k in range(M//2):
#                 if a[i][j+k] != a[i][j + M - 1 - k]:
#                     p = ''
#                     break
#                 else:
#                     p = a[i]
#             else:
#                 print(p)
#     # print(p)
#
def nums():
    p = ''
    for num in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if a[num][j+k] != a[num][j + M - 1 - k]:
                    break

            else:
                for i in range(j, j+M):
                    p += a[num][i]
                return p

    for num in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if a[j+k][num] != a[j + M - 1 - k][num]:
                    break

            else:
                for i in range(j, j+M):
                    p += a[i][num]
                return p

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    a = [input() for _ in range(N)]

    print(f'#{tc+1} {nums()}')





