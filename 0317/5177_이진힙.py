import sys
sys.stdin = open('5177.txt')


def enq(n):
    global last
    last += 1
    h_arr[last] = n
    c = last
    p = c // 2
    while p and h_arr[p] > h_arr[c]:
        h_arr[p], h_arr[c] = h_arr[c], h_arr[p]
        c = p
        p = c // 2


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    h_arr = [0] * (N+1)
    last = 0

    for i in arr:
        enq(i)

    num_sum = 0
    while last > 0:
        last = last // 2
        num_sum += h_arr[last]

    print(f'#{tc+1} {num_sum}')