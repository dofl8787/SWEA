import sys
sys.stdin = open('9517.txt')

K = int(input()) - 1
N = int(input())

total_sec = 210

for i in range(N):
    sec, ans = input().split()
    sec = int(sec)

    if total_sec > 0:
        if ans == 'T':
            total_sec -= sec
            if K == 8:
                K = 1
            else:
                K +=1
        elif ans == 'N' or ans == 'F':
            total_sec -= sec
    else:
        break
print(K)