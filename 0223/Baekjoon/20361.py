import sys
sys.stdin = open('20361.txt')

N, X, K = map(int, input().split())

arr = [0] * (N+1)
arr[X] = 1

for i in range(K):
    n,m = map(int, input().split())
    arr[n],arr[m] = arr[m],arr[n]

for j in range(len(arr)):
    if arr[j] == 1:
        print(j)