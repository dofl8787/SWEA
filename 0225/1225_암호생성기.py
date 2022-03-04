import sys
sys.stdin = open('1225.txt')






def make_pw(lst):
    while 1:
        for number in range(1,6):
            num = lst.pop(0) - number
            lst.append(num)

            if lst[-1] <= 0:
                lst[-1] = 0
                return lst

for tc in range(10):
    n = input()
    text = list(map(int, input().split()))

    print(f'#{tc+1}', *make_pw(text))




