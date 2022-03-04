N,M = map(int, input().split())

basket = [0]* (N+1) #0으로 시작하기 때문에 빈 바구니 N개 설정

for _ in range(M):
    st,ed, num = map(int, input().split())

    for i in range(st,ed+1): #시작부터 끝까지 같은 숫자로 덮기 때문에 for
        basket[i] = num #새로 숫자가 들어오면 덮어씌우기

print(*basket[1:])