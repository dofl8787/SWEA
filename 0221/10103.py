import sys
sys.stdin = open('10103.txt')

n = int(input())

c_score = s_score = 100
for i in range(n):
    c,s = list(map(int, input().split()))
    if c < s:
        c_score -= s
    elif c == s:
        pass
    elif c > s:
        s_score -= c
print(c_score)
print(s_score)