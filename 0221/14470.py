import sys
sys.stdin = open('14470.txt')


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


cnt_m = cnt_p = 0
for i in range(a, b):
    if a < 0:
        if i < 0:
            cnt_m += 1
        elif i >= 0:
            cnt_p += 1
        result = (cnt_m * c) + d + (cnt_p * e)
    else:
        cnt_p += 1
        result = cnt_p*e


print(result)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
#
# total = 0
# if a < 0:
#     total = (-a)*c + d + b*e
#
# else:
#     total = (b-a)*e