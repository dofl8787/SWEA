import sys
sys.stdin = open('3499.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input().split()
    #덱을 두 개로 나누기
    mid = N //2
    remain = []
    if N % 2 == 0:
        deck1 = cards[:mid]
        deck2 = cards[mid:]
    else:
        deck1 = cards[:mid+1]
        deck2 = cards[mid+1:]
        remain.append(deck1[-1])

    #deck1에서 하나, deck2에서 하나씩 순서대로 붙이기
    result = []
    for i in range(mid):
        result.append(deck1[i])
        result.append(deck2[i])
    print(f'{tc}', *(result + remain))