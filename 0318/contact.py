import sys
sys.stdin = open('contact.txt')

N,M = map(int, input().split())
lst = list(map(int, input().split()))

arr = [0] * (N+1)

visit = [0] *(N+1)

#
# for i in range(N):
#     if i == 0:
#         arr[i] = :
#     else:
#         arr[i] =