N, M, L = map(int, input().split())

friends = [0] * N
ball = 0
cnt = 0
while True:
    friends[ball] += 1

    if friends[ball] == M:
        break

    if friends[ball] % 2 == 1:
        ball = (ball+L) % N
        cnt += 1
    else:
        ball = (ball+(N-L)) % N
        cnt += 1

print(cnt)