n = int(input())
num = 1
while n > 1:
    if n % 2 == 0:
        n = n/2
        num += 1
    elif n % 2 == 1:
        n = 3 * n + 1
        num += 1
print(num)