import sys
sys.stdin = open('a.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(str, input()))+ [0] for _ in range(N)]
    arr.append([0]*(N+1))

    a= len(arr)
    new_arr = []
    result = 0
    for i in range(a):
        for j in range(a):
            if arr[i][j] == 'o':
                new_arr.append(arr[i][j])
            elif arr[i][j] == '.':
                b = len(new_arr)
                if b == N:
                    print('Yes')
                    break
                else:
                    new_arr = []

