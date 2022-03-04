import sys
sys.stdin = open('GNS.txt')


T = int(input())
for _ in range(T):
    tst_n , N =input().split()
    arr = list(input().split())
    N = int(N)
    lst_a = [0] * 10 # 카운트 배열
    lst_b = [0] * N # 정렬된 배열
    A_dict = { "ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7,"EGT":8, "NIN":9 }
    for i in arr:
        lst_a[A_dict[i]] += 1

    for j in range(1, 10):
        lst_a[j] += lst_a[j-1]

    for k in range(len(lst_b)-1, -1, -1):
        lst_a[A_dict[arr[k]]] -=1
        lst_b[lst_a[A_dict[arr[k]]]] = arr[k]

    print(f'{tst_n} \n', *lst_b)


