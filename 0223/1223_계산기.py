import sys
sys.stdin = open('1223.txt')

T = 10
for tc in range(T):
    N = int(input())
    text = input()
    postfix = []
    S = []

    icp = {'+': 1, '*':2, '(':3}
    isp = {'+': 1, '*':2, '(':0 }

    for num in text:
        if num in icp:
            while S and isp[S[-1]] > icp[num]:
                postfix.append(S.pop())
            S.append(num)
        elif num == ')':
            while S and S[-1] != '(':
                postfix.append(S.pop())
            S.pop()

        else:
            postfix.append(num)
    while S:
        postfix.append(S.pop())

    for num in postfix:
        if num in icp:
            b = S.pop()
            a = S.pop()
            if num == '+':
                S.append(a+b)
            else:
                S.append(a*b)
        else:
            S.append(int(num))
    print(f'#{tc+1}', *S)