import sys
sys.stdin = open('12756.txt')

A = list(map(int, input().split()))
B = list(map(int, input().split()))

num_a = A[1]
num_aa = A[0]
num_b = B[1]
num_bb = B[0]
while True:
    if B[1] >= 0 or A[-1] >= 0:
        B[1] = B[1] - A[0]
        A[1] = A[1] - B[0]
    if int(num_a) <= 0:
        print('PLAYER B')
    elif int(num_b) <= 0:
        print('PLAYER A')
    elif num_a <= 0 and num_b <= 0:
        print('DRAW')