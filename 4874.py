import sys
sys.stdin = open('4874.txt')

def Forth(text):
    num_lst = []
    icp = ['/', '+', '-', '*']
    for i in text:
        if i == '.':
            if len(num_lst) != 1:
                return 'error'
        elif i in icp:
            if len(num_lst) < 2:
                return 'error'
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
        return ('error')
    else:
        return num_lst[0]

T= int(input())

for tc in range(T):
    text = input().split()
    print(f'#{tc+1} {Forth(text)}')