import sys
sys.stdin = open('a.txt')

for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 0
        n_lst = []
        for j in range(N):
            if arr[j][i] == 1:
                n_lst.append(arr[j][i])
            elif arr[j][i] == 2:
                if n_lst:
                    cnt += 1
                    n_lst = []
            else:
                continue
        result += cnt

    print(result)