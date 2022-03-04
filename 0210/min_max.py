# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
#
#
# [입력]
#
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
#
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
#
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
#
# [출력]
#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
import sys
sys.stdin = open('min_max.txt')

T = int(input()) #전체 케이스 개수 각 케이스 양수 개수


for i in range(T):
    N = int(input())
    ai = list(map(int, input().split()))
    max_num = min_num = ai[0]
    for j in range(N):
        if max_num < ai[j]:
            max_num = ai[j]
        if min_num > ai[j]:
            min_num = ai[j]
    print(f' #{i+1} {max_num - min_num}')

# for i in range(T):
#     N = int(input())
#     for J in range(N):
#         ai = list(map(int, input().split()))
#         print(ai)

