import sys
sys.stdin = open('1547.txt')


M = int(input())
cup = [1, 2, 3]

for i in range(M):
    x, y = map(int, input().split())
    cup[x-1], cup[y-1] = cup[y-1], cup[x-1]

for j in range(3):
    if cup[j] == 1:
        print(j+1)
