N, M = map(int, input().split())
arr = [i+1 for i in range(N)]


for _ in range(M):
    num1, num2 = map(int, input().split())
    arr[num1-1], arr[num2-1] = arr[num2-1], arr[num1-1]

print(*arr)