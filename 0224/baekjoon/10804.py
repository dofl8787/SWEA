

arr = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    for j in range((b-a+1)//2):
        arr[a+j], arr[b-j] = arr[b-j], arr[a+j]
print(*arr[1:])