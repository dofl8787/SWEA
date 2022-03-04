N, M, L = map(int, input().split())


people = [0 for _ in range(N+1)]

cnt = 0
people[1] = 1
print(people)
for num in range(len(people)):
    while people[num] != M:
        people[num] += 1


