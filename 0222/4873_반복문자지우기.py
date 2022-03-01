import sys
sys.stdin = open('4873.txt')

T = int(input())

for tc in range(T):
    text = list(input())

    new_arr = []
    for i in text:
        if i not in new_arr:
            new_arr.append(i)
        elif i != new_arr[-1]:
            new_arr.append(i)
        else:
            new_arr.pop()
    print(f'#{tc+1} {len(new_arr)}')