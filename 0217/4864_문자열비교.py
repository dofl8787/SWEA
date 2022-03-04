import sys
sys.stdin = open('4864.txt')

T= int(input())

for tc in range(T):
    str1 = input()
    str2 = input()

    m, n = len(str1), len(str2)
    i = j = 0
    while j < m and i < n:
        if str1[j] != str2[i]:
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1
    if j == m:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')