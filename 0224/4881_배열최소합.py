def perm(k, cur_sum): # cur_sum : 지금까지 선택한 요소들의 합
    global ans
    if cur_sum >= ans: #가지치기
        return
    if k == N:
        if ans > cur_sum:
            ans = cur_sum
    else:
        for i in range(k, N):
            cols[k], cols[i] = cols[i], cols[k]
            perm(k + 1, cur_sum + arr[k][cols[k]])   # arr[k][cols[k]]
            cols[k], cols[i] = cols[i], cols[k]


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cols = [i for i in range(N)]
    ans = 9999999999
    perm(0, 0)
    print(f'#{tc+1} {ans}')