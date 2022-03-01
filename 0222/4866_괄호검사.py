import sys
sys.stdin = open('4866.txt')

T = int(input())
result = 0
for tc in range(T):
    text = input()
    t_lst = []
    for i in text:
        if i == '(' or i == '{':
            t_lst.append(i)
        elif i == ')' or i == '}':
            if len(t_lst) == 0:
                result = 0
                break
            elif i == ')' and t_lst.pop() != '(':
                result = 0
                break
            elif i == '}' and t_lst.pop() != '{':
                result = 0
                break
        else:
            result = 1

    if len(t_lst) != 0:
        result = 0
    print(f'#{tc+1} {result}')
