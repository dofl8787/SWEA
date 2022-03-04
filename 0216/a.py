a = [4,9,1,4,4,2]
b = [1,3,4,2,5,6,7,8,9]

for i in range(len(b)):
    # if b[i] in a:
    #     print('o')
    # else:
    #     print('x')
    flag =0
    for j in range(len(a)):
        if a[j] == b[i]:
            flag = 1
            break
    if flag == 1:
        print('o', end=' ')
    else:
        print('X', end= ' ')