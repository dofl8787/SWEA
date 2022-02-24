import sys
sys.stdin = open('4874.txt')

T= int(input())

for tc in range(T):
    text = input().split()
    num_lst = []
    icp = ['/', '+', '-', '*']
    for i in text:
        if i == '.':
            if len(num_lst) != 1:
                print(f'#{(tc+1)} error')
                break
        elif i in icp:
            if len(num_lst) < 2:
                print(f'#{(tc+1)} error')
                break
            b = int(num_lst.pop())
            a = int(num_lst.pop())
            if i == '/':
                num_lst.append(a // b)
            elif i == '*':
                num_lst.append(a * b)
            elif i == '+':
                num_lst.append(a + b)
            elif i == '-':
                num_lst.append(a - b)
        else:
            num_lst.append(int(i))

    if len(num_lst) != 1:
        print('error')
    else:
        print(f'#{(tc+1)} {num_lst[0]}')

